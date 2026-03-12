# Manifesto

Back to the front page: [README.md](README.md)

Free software must not become surveillance infrastructure.

We reject every attempt to turn general-purpose operating systems into systems for classification, inspection, filtering, disclosure, or control. We reject these attempts whether they arrive under the language of age verification, age signaling, child safety, lawful access, platform responsibility, or any other softer name chosen to disguise the same underlying mechanism.

This project exists because a line is being crossed.

That line is crossed when free software distributions are pressured to collect age-related data at installation or provisioning time. It is crossed when account metadata services are repurposed to store that data. It is crossed when portals and standard APIs are designed to expose it. It is crossed when application and service ecosystems begin assuming that the operating system should provide user classification as a normal function.

We reject that entire category of change.

## What we reject

We reject:

- OS-level age verification
- age signaling and age-bracket APIs
- client-side scanning and device-side inspection
- metadata layers repurposed for compliance
- portals repurposed for surveillance or classification
- downstream inheritance of surveillance mechanisms
- geo-fencing users out of free software
- the normalization of policy-enforcement endpoints inside general-purpose systems

We reject them not because they are poorly implemented, but because they should not exist in free software distributions at all.

There is no acceptable implementation path.

Not in the installer.  
Not in provisioning.  
Not in account metadata.  
Not in user databases.  
Not in portals.  
Not in app-facing APIs.  
Not as a minimal age bracket.  
Not as an opaque token.  
Not as a temporary measure.  
Not as a jurisdiction-specific compromise.  
Not in any form.

## The trap

The trap is always the same.

First comes a law, a proposal, or a political demand presented as urgent and morally unquestionable. Then comes the rhetoric: protect the children, protect the public, protect society, protect users. Then comes the pressure on technical communities to help design, package, normalize, and quietly ship the mechanism.

And once that process begins, the debate is no longer about whether the mechanism should exist. It becomes a debate about where to store it, how to expose it, how to package it, and how to make it easier to update or remove later.

That is the trap.

The most serious mistake is not a particular schema, daemon, field name, D-Bus interface, or packaging choice. The most serious mistake is accepting the premise that free software projects should be discussing how to build these mechanisms at all.

We reject that premise.

## The rhetoric of coercion

These mechanisms are often advanced through emotional blackmail.

A universally sympathetic objective is invoked. Urgency is manufactured. Technical resistance is framed as moral failure. Objections to surveillance are treated as if they were objections to safety itself.

We reject that coercive framing.

Protecting children is a serious obligation. Public safety is a serious obligation. Neither obligation authorizes the transformation of free software into surveillance machinery. Neither obligation grants states, platforms, or third parties a moral right to force classification and inspection mechanisms into systems that should remain under user control.

The use of emotional leverage does not legitimize the mechanism. It is one more reason to refuse it.

## Free software belongs to users

Free software exists so that users can understand, control, modify, and share the systems they depend on.

It does not exist to become a policy-enforcement layer for the state.  
It does not exist to become a compliance substrate for app stores or service providers.  
It does not exist to become a classification system for age, identity, or legal status.  
It does not exist to become a scanning surface for automated inspection.

A free operating system must remain a general-purpose system under user control.

The moment it becomes a platform for classifying or exposing users to third-party services by design, it has been pushed in the wrong direction.

## No law is above morality

A law can create pressure. It cannot create legitimacy.

A law can threaten maintainers, distributions, or platforms. It cannot transform an illegitimate surveillance mechanism into an acceptable one.

No law is above morality.  
No law is above technical scrutiny.  
No law obligates free software communities to normalize what they should reject.

The existence of a legal demand is not the end of the argument. It is often the beginning of the most important argument.

## No implementation and no geo-fencing

This project rejects both of the false choices often presented in these situations.

The first false choice is implementation: quietly add the mechanism and pretend the damage is limited.

The second false choice is geo-fencing: deny users access to free software based on where they live and pretend the moral problem has been solved by excluding them.

We reject both.

Free software must not ship surveillance mechanisms.  
Free software must also not abandon users by jurisdiction.

Neither implementation nor geo-fencing is acceptable.

## Our red line

The first concrete implementation step is already too far.

The red line is crossed when a project adds an age-related field to an installer or provisioning flow.  
The red line is crossed when age-related data is added to account metadata or user records.  
The red line is crossed when a portal or API is created to expose such data.  
The red line is crossed when downstream distributions inherit these mechanisms without stripping them.

There is no safe first step toward building this apparatus. The first step is already the wrong step.

## What we will do

We will document every relevant law, proposal, issue, pull request, merge request, discussion, and code path.

We will map the architecture through which these mechanisms spread.

We will identify the components that normalize them.

We will oppose them publicly.

We will refuse their normalization.

We will prepare downstream removal and package-level stripping where upstream projects merge them.

We will teach users and maintainers how to identify, remove, replace, rebuild, and distribute clean packages.

Where necessary, we will maintain deltas, patch sets, and forks to keep free software distributions free of surveillance mechanisms.

We will not quietly adapt to this.

## What this project stands for

This project stands for:

- user control over computing systems
- general-purpose operating systems free of surveillance roles
- resistance to coercive legal and political normalization
- transparency in documenting every implementation path
- downstream removal where upstream fails
- universal access to free software without surveillance and without geo-fencing

This is not a neutral archive.

It is a public refusal.
It is a technical dossier.
It is a map for reversal work.
It is a commitment to keep free software free.

## Final declaration

Free software distributions must not become surveillance infrastructure.

We will document what is being built.  
We will expose how it spreads.  
We will refuse its normalization.  
We will remove it where it lands.  
We will rebuild what is necessary.  
We will teach others to do the same.

Document. Refuse. Remove. Rebuild.

## See also

- [README.md](README.md)
- [TRACKER.md](TRACKER.md)
- [LAWS.md](LAWS.md)
- [STACK.md](STACK.md)
- [REPO-TARGETS.md](REPO-TARGETS.md)
- [REVERSIONS/README.md](REVERSIONS/README.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
