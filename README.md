# Awesome Chained Tool-Calling Agents

A curated collection of research papers, datasets, tools, implementations, and learning resources related to failure modes in chained tool-calling agents operating without human checkpoints.

This repository focuses on reliability, security, error propagation, prompt injection, state tracking, tool misuse, and verification challenges in autonomous LLM-based agents.

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
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [License](#license)

## Overview

Chained tool-calling agents are AI systems that repeatedly reason, invoke external tools, observe results, update their state, and perform subsequent actions. While this allows large language model (LLM) agents to perform complex tasks, removing human checkpoints can make small errors propagate across multiple steps.

Important failure modes include incorrect planning, wrong tool selection, argument and schema errors, state-tracking failures, error propagation, feedback-loop failures, instruction and context drift, indirect prompt injection, excessive agency, data exfiltration, and memory poisoning.

This repository collects verified research and practical resources related to these problems. It is intended to help students and researchers understand how autonomous tool-calling agents fail, how these failures can be evaluated, and what techniques can improve the reliability and security of long-horizon agent execution.

## AI-Assisted Research Paper

**Title:** Failure Modes in Chained Tool-Calling Agents Operating Without Human Checkpoints

This research paper examines reliability and security failures that can emerge when LLM agents perform sequences of tool calls without human checkpoints.

[View AI-Assisted Research Paper](paper/AI_Assisted_Research_Paper.pdf)

## Citation Integrity Audit

The accompanying citation-integrity audit examines whether AI-generated references actually exist, whether their bibliographic metadata are correct, and whether cited sources support the claims for which they were used.

[View Citation Integrity Audit](citation-audit/Citation_Integrity_Audit.pdf)

## Survey and Review Papers

Research papers that provide broad perspectives on LLM agents, tool use, reliability, and security.

See [references/references.md](references/references.md).

## Foundational Papers

Important foundational research on tool-augmented language models, reasoning and acting, and autonomous agents.

See [references/references.md](references/references.md).

## Recent Research Papers

Recent research addressing long-horizon execution, agent safety, tool-use security, and verification.

See [references/references.md](references/references.md).

## Agent Security

Research concerning prompt injection, excessive agency, data exfiltration, memory poisoning, and other security risks in tool-integrated agents.

See [references/references.md](references/references.md).

## Benchmarks and Evaluation

Benchmarks and evaluation environments for testing autonomous agents and long-horizon task execution.

See [datasets/datasets.md](datasets/datasets.md).

## Datasets

Relevant datasets and benchmarks for studying LLM agents and tool-calling systems.

See [datasets/datasets.md](datasets/datasets.md).

## Tools and Libraries

Useful frameworks, tools, and libraries for developing or studying LLM-based agents and tool calling.

See [tools/tools.md](tools/tools.md).

## GitHub Implementations

Open-source implementations related to LLM agents, tool calling, benchmarks, and agent security.

See [implementations/github-repositories.md](implementations/github-repositories.md).

## Tutorials and Learning Resources

Authoritative documentation, tutorials, lectures, and other learning resources related to LLM agents and AI security.

## License

This repository is provided for academic and educational purposes.
