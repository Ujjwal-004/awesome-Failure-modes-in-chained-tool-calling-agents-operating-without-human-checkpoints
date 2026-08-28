# Awesome Chained Tool-Calling Agents

A curated collection of research papers, datasets, tools, implementations,
and learning resources related to failure modes in chained tool-calling
agents operating without human checkpoints.

This repository focuses on reliability, security, error propagation, prompt
injection, state tracking, tool misuse, memory, planning, and verification
challenges in autonomous LLM-based agents.

## Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Survey and Review Papers](#survey-and-review-papers)
- [Foundational Papers](#foundational-papers)
- [Recent Research Papers](#recent-research-papers)
- [Agent Security](#agent-security)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [Implementation](#implementation)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [Research Themes](#research-themes)
- [License](#license)

## Overview

Chained tool-calling agents are AI systems that repeatedly reason, invoke
external tools, observe results, update their state, and perform subsequent
actions.

While this allows large language model (LLM) agents to perform complex
tasks, removing human checkpoints can allow small errors to propagate across
multiple steps.

Important failure modes include:

- Incorrect planning
- Incorrect tool selection
- Tool argument and schema errors
- State-tracking failures
- Error propagation
- Feedback-loop failures
- Instruction and context drift
- Indirect prompt injection
- Excessive agency
- Data exfiltration
- Memory poisoning
- Lack of verification
- Unsafe autonomous actions

This repository collects research and practical resources related to these
problems. It is intended to help students and researchers understand how
autonomous tool-calling agents fail, how these failures can be evaluated,
and what techniques can improve the reliability and security of long-horizon
agent execution.

## AI-Assisted Research Paper

**Title:** Failure Modes in Chained Tool-Calling Agents Operating Without
Human Checkpoints

This research paper examines reliability and security failures that can
emerge when LLM agents perform sequences of tool calls without human
checkpoints.

[View AI-Assisted Research Paper](paper/AI_Assisted_Research_Paper.pdf)

## Citation Integrity Audit

The accompanying citation-integrity audit examines whether AI-generated
references exist, whether their bibliographic metadata are correct, and
whether cited sources support the claims for which they were used.

[View Citation Integrity Audit](citation-audit/Citation_Integrity_Audit.pdf)

## Survey and Review Papers

Research papers that provide broad perspectives on LLM agents, tool use,
reliability, planning, memory, and security.

See [references/references.md](references/references.md).

## Foundational Papers

Important foundational research on tool-augmented language models,
reasoning and acting, autonomous agents, and multi-step reasoning.

See [references/references.md](references/references.md).

## Recent Research Papers

Recent research addressing long-horizon execution, agent safety, tool-use
security, prompt injection, verification, and agent evaluation.

See [references/references.md](references/references.md).

## Agent Security

Research concerning prompt injection, indirect prompt injection, excessive
agency, data exfiltration, memory poisoning, and other security risks in
tool-integrated agents.

See [references/references.md](references/references.md).

## Benchmarks and Evaluation

Benchmarks and evaluation environments for testing autonomous agents,
tool-calling systems, web agents, security, and long-horizon task execution.

See [datasets/README.md](datasets/README.md).

## Datasets

Relevant datasets and benchmark environments for studying LLM agents,
tool-calling systems, web interaction, security, and multi-step execution.

The dataset resources include:

- WebArena
- AgentDojo
- AgentBench
- Mind2Web
- BrowserGym

See [datasets/README.md](datasets/README.md).

## Tools and Libraries

Useful frameworks, tools, libraries, and engineering resources for
developing, evaluating, monitoring, and securing LLM-based agents and
tool-calling systems.

Resources include areas such as:

- Agent frameworks
- Tool-calling frameworks
- Browser automation
- Security testing
- Guardrails
- Human approval
- Monitoring and tracing
- Evaluation
- Verification

See [tools/README.md](tools/README.md).

## Implementation

Implementation guidance for building, testing, and evaluating reliable
chained tool-calling agents operating without human checkpoints.

Topics include:

- Agent execution pipelines
- Tool input validation
- Tool output validation
- Error propagation control
- State tracking
- Human checkpoints
- Guardrails
- Prompt-injection defenses
- Verification
- Logging and tracing
- Failure recovery
- Testing strategies
- Evaluation metrics

See [implementation/README.md](implementation/README.md).

## GitHub Implementations

Open-source implementations and repositories related to LLM agents,
tool calling, benchmarks, web agents, and agent security.

Where possible, implementation resources should be connected to the
corresponding research papers and official project repositories.

## Tutorials and Learning Resources

Authoritative documentation, tutorials, lectures, and other learning
resources related to LLM agents, tool calling, agent security, evaluation,
and reliable autonomous execution.

Useful learning areas include:

- Tool calling
- Agent architectures
- Agent evaluation
- Prompt injection
- Guardrails
- Human-in-the-loop systems
- Agent memory
- Web-agent development
- Security testing
- Monitoring and tracing

## Research Themes

The repository organizes resources around the following research themes:

- Tool misuse
- Incorrect tool selection
- Error propagation
- Hallucinated intermediate results
- Prompt injection
- Indirect prompt injection
- Memory poisoning
- Planning failures
- State-tracking failures
- Lack of verification
- Unsafe autonomous actions
- Lack of human checkpoints
- Agent security and robustness
- Multi-step task failure
- Self-correction and reflection

## Repository Structure

```text
.
├── citation-audit/
│   └── Citation_Integrity_Audit.pdf
│
├── datasets/
│   └── README.md
│
├── implementation/
│   └── README.md
│
├── paper/
│   └── AI_Assisted_Research_Paper.pdf
│
├── references/
│   └── references.md
│
├── tools/
│   └── README.md
│
└── README.md
