#!/usr/bin/env python3

# Author: Thiago Camargo <thiagocmc@proton.me>

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

CANONICAL_FILES = [
    "README.md",
    "MANIFESTO.md",
    "TRACKER.md",
    "LAWS.md",
    "STACK.md",
    "REPO-TARGETS.md",
    "CONTRIBUTING.md",
    "REVERSIONS/README.md",
]

README_REQUIRED_LINKS = [
    "README.md",
    "MANIFESTO.md",
    "TRACKER.md",
    "LAWS.md",
    "STACK.md",
    "REPO-TARGETS.md",
    "REVERSIONS/README.md",
    "CONTRIBUTING.md",
]

REQUIRED_SECTIONS = {
    "README.md": [
        "Mission",
        "Repository map",
        "Principles",
    ],
    "MANIFESTO.md": [
        "What we reject",
        "The trap",
        "What we will do",
    ],
    "TRACKER.md": [
        "Purpose",
        "Status labels",
        "Current evidence index",
    ],
    "LAWS.md": [
        "Purpose",
        "Current legal and policy drivers",
    ],
    "STACK.md": [
        "Purpose",
        "Core propagation path",
    ],
    "REPO-TARGETS.md": [
        "Purpose",
        "Current targets",
    ],
    "CONTRIBUTING.md": [
        "Purpose",
        "Contribution standards",
        "Internal link discipline",
    ],
    "REVERSIONS/README.md": [
        "Purpose",
        "Current strategy",
    ],
}

PREFERRED_TERMS = [
    "OS-level age verification",
    "age signaling",
    "age-bracket API",
    "surveillance mechanism",
    "policy-enforcement endpoint",
    "downstream removal",
    "geo-fencing",
]

BANNED_PATTERNS = {
    r"\bwithout scrutiny\b": "Use an absolute formulation instead of implying surveillance could be acceptable if reviewed.",
    r"\bcompliance functionality\b": "Avoid framing the mechanism as a neutral compliance feature.",
    r"\bsurveillance functionality\b": "Prefer 'surveillance mechanisms' to reflect the full apparatus.",
}

# Standard inline markdown link, excluding images.
INLINE_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
HEADER_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
CODE_FENCE_RE = re.compile(r"^\s*(```|~~~)")
TRACKER_TABLE_ROW_RE = re.compile(r"^\|\s*(.*?)\s*\|$")
URL_RE = re.compile(r"https?://[^\s)>]+")


@dataclass
class Finding:
    level: str
    file: str
    message: str
    line: int | None = None

    def format(self) -> str:
        location = self.file
        if self.line is not None:
            location += f":{self.line}"
        return f"[{self.level}] {location} - {self.message}"


class Auditor:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.findings: list[Finding] = []
        self.link_graph: dict[str, set[str]] = defaultdict(set)
        self.backlinks: Counter[str] = Counter()
        self.documents: dict[str, list[str]] = {}

    def add(self, level: str, file: str, message: str, line: int | None = None) -> None:
        self.findings.append(Finding(level, file, message, line))

    def relative(self, path: Path) -> str:
        return path.relative_to(self.root).as_posix()

    def read_documents(self) -> None:
        for rel in CANONICAL_FILES:
            path = self.root / rel
            if not path.exists():
                self.add("ERROR", rel, "Canonical file is missing.")
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except Exception as exc:
                self.add("ERROR", rel, f"Failed to read file: {exc}")
                continue
            self.documents[rel] = text.splitlines()

        # Flag extra markdown files that are not in the canonical set.
        extras = []
        for path in self.root.rglob("*.md"):
            rel = self.relative(path)
            if rel not in CANONICAL_FILES:
                extras.append(rel)
        for rel in sorted(extras):
            self.add("WARN", rel, "Markdown file is outside the canonical document set; ensure it is intentional and discoverable.")

    def audit(self) -> int:
        self.read_documents()
        for rel, lines in self.documents.items():
            self.audit_file(rel, lines)
        self.audit_canonical_links()
        self.audit_discoverability()
        self.audit_readme_structure()
        self.audit_terminology_presence()
        return 1 if any(f.level == "ERROR" for f in self.findings) else 0

    def audit_file(self, rel: str, lines: list[str]) -> None:
        self.check_required_sections(rel, lines)
        self.check_code_fences(rel, lines)
        self.check_headings(rel, lines)
        self.check_banned_patterns(rel, lines)
        self.check_links(rel, lines)
        if rel == "TRACKER.md":
            self.check_tracker_links(rel, lines)
        if rel == "REPO-TARGETS.md":
            self.check_repo_targets_links(rel, lines)

    def check_required_sections(self, rel: str, lines: list[str]) -> None:
        headers = {m.group(2).strip() for line in lines if (m := HEADER_RE.match(line))}
        for section in REQUIRED_SECTIONS.get(rel, []):
            if section not in headers:
                self.add("ERROR", rel, f"Missing required section: '{section}'.")

    def check_code_fences(self, rel: str, lines: list[str]) -> None:
        for idx, line in enumerate(lines, start=1):
            if CODE_FENCE_RE.match(line):
                self.add("WARN", rel, "Code fence found; prose-first Markdown is preferred for this document set.", idx)

    def check_headings(self, rel: str, lines: list[str]) -> None:
        prev_level = 0
        seen_h1 = False
        for idx, line in enumerate(lines, start=1):
            match = HEADER_RE.match(line)
            if not match:
                continue
            level = len(match.group(1))
            if level == 1:
                if seen_h1:
                    self.add("WARN", rel, "Multiple H1 headings found.", idx)
                seen_h1 = True
            if prev_level and level > prev_level + 1:
                self.add("WARN", rel, f"Heading jumps from H{prev_level} to H{level}.", idx)
            prev_level = level
        if not seen_h1:
            self.add("ERROR", rel, "Missing H1 heading.")

    def check_banned_patterns(self, rel: str, lines: list[str]) -> None:
        for idx, line in enumerate(lines, start=1):
            for pattern, reason in BANNED_PATTERNS.items():
                if re.search(pattern, line, flags=re.IGNORECASE):
                    self.add("WARN", rel, reason, idx)

    def check_links(self, rel: str, lines: list[str]) -> None:
        file_path = self.root / rel
        text = "\n".join(lines)
        for match in INLINE_LINK_RE.finditer(text):
            target = match.group(2).strip()
            line = text[: match.start()].count("\n") + 1
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                continue
            target_path = target.split("#", 1)[0]
            resolved = (file_path.parent / target_path).resolve()
            try:
                resolved.relative_to(self.root.resolve())
            except ValueError:
                self.add("ERROR", rel, f"Relative link escapes repository root: {target}", line)
                continue
            if not resolved.exists():
                self.add("ERROR", rel, f"Broken internal link: {target}", line)
                continue
            target_rel = self.relative(resolved)
            self.link_graph[rel].add(target_rel)
            self.backlinks[target_rel] += 1

    def check_tracker_links(self, rel: str, lines: list[str]) -> None:
        in_table = False
        for idx, line in enumerate(lines, start=1):
            if line.startswith("| Component | Repository | Item | Status |"):
                in_table = True
                continue
            if in_table and not line.startswith("|"):
                in_table = False
            if not in_table or idx <= 1:
                continue
            if line.startswith("| ---"):
                continue
            # Require at least one external direct link per row.
            if "http://" not in line and "https://" not in line:
                self.add("ERROR", rel, "Tracker row lacks a direct source link.", idx)

    def check_repo_targets_links(self, rel: str, lines: list[str]) -> None:
        current_section = None
        section_has_link = defaultdict(bool)
        for idx, line in enumerate(lines, start=1):
            match = HEADER_RE.match(line)
            if match and len(match.group(1)) == 3:
                current_section = match.group(2).strip()
                continue
            if current_section and URL_RE.search(line):
                section_has_link[current_section] = True
        # Skip non-component H3s.
        h3_sections = set()
        for line in lines:
            match = HEADER_RE.match(line)
            if match and len(match.group(1)) == 3:
                h3_sections.add(match.group(2).strip())
        component_sections = {
            s for s in (set(section_has_link.keys()) | h3_sections)
            if s not in {"Watchlist concept", "How this file differs from the tracker"}
        }
        for section in sorted(component_sections):
            if not section_has_link[section]:
                self.add("WARN", rel, f"Component section '{section}' lacks direct upstream references.")

    def audit_canonical_links(self) -> None:
        readme_links = self.link_graph.get("README.md", set())
        for rel in README_REQUIRED_LINKS:
            if rel == "README.md":
                continue
            if rel not in readme_links:
                self.add("ERROR", "README.md", f"Repository map should link to {rel}.")

    def audit_discoverability(self) -> None:
        for rel in CANONICAL_FILES:
            if rel == "README.md":
                continue
            if rel not in self.documents:
                continue
            if self.backlinks[rel] == 0:
                self.add("ERROR", rel, "Document is dangling; no inbound internal links found.")

    def audit_readme_structure(self) -> None:
        lines = self.documents.get("README.md")
        if not lines:
            return
        text = "\n".join(lines)
        repo_map_index = text.find("## Repository map")
        if repo_map_index == -1:
            return
        for target in README_REQUIRED_LINKS:
            if target == "README.md":
                continue
            if f"({target})" not in text[repo_map_index:]:
                self.add("WARN", "README.md", f"Repository map may be missing explicit link to {target}.")

    def audit_terminology_presence(self) -> None:
        corpus = "\n".join("\n".join(lines) for lines in self.documents.values())
        for term in PREFERRED_TERMS:
            if term not in corpus:
                self.add("WARN", "<project>", f"Preferred term not found anywhere in document set: '{term}'.")


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Audit OSS Anti Surveillance Markdown docs.")
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root to audit (default: current directory).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on warnings as well as errors.",
    )
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    auditor = Auditor(root)
    exit_code = auditor.audit()

    if auditor.findings:
        for finding in auditor.findings:
            print(finding.format())
    else:
        print("Audit passed with no findings.")

    if args.strict and auditor.findings:
        return 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
