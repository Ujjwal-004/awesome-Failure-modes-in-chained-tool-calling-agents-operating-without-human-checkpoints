# Datasets and Benchmarks

Datasets and benchmark environments relevant to chained tool-calling
agents, agent reliability, multi-step execution, web interaction,
security, and prompt injection.

## 1. WebArena

**Purpose:** Realistic web-agent evaluation.

WebArena is a self-hostable environment for building and evaluating
autonomous agents on realistic websites and multi-step tasks.

- Repository: https://github.com/web-arena-x/webarena
- Paper: "WebArena: A Realistic Web Environment for Building Autonomous Agents"
- arXiv: 2307.13854
- Relevance:
  - Multi-step web interaction
  - Tool/action selection
  - Long-horizon execution
  - State tracking
  - Task completion failures

## 2. AgentDojo

**Purpose:** Security and prompt-injection evaluation.

AgentDojo is a dynamic environment for evaluating attacks and defenses
for LLM agents operating with tools and untrusted data.

- Repository: https://github.com/ethz-spylab/agentdojo
- Paper: "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection
  Attacks and Defenses for LLM Agents"
- Year: 2024
- Relevance:
  - Indirect prompt injection
  - Tool misuse
  - Security failures
  - Defense evaluation
  - Agent behavior under adversarial conditions

## 3. AgentBench

**Purpose:** General evaluation of LLM agents.

AgentBench provides a benchmark framework for evaluating LLMs as agents
across multiple environments and task types.

- Repository: https://github.com/THUDM/AgentBench
- Paper: "AgentBench: A Comprehensive Benchmark to Evaluate LLMs as Agents"
- Conference: ICLR 2024
- Relevance:
  - Agent evaluation
  - Multi-step tasks
  - Tool interaction
  - Environment-based evaluation

## 4. Mind2Web

**Purpose:** Generalist web-agent evaluation.

Mind2Web is a dataset for developing and evaluating agents that follow
language instructions to complete complex tasks on real-world websites.

- Repository: https://github.com/OSU-NLP-Group/Mind2Web
- Paper: "Mind2Web: Towards a Generalist Agent for the Web"
- Conference: NeurIPS 2023
- Relevance:
  - Long-horizon web tasks
  - Action sequences
  - Real-world websites
  - Multi-step interaction
  - Generalist web agents

## 5. BrowserGym

**Purpose:** Unified environment for web-agent research.

BrowserGym provides a Gymnasium-compatible environment and integrates
multiple web-agent benchmarks.

Included benchmarks include WebArena, WebArenaVerified,
VisualWebArena, WorkArena, MiniWoB++, AssistantBench, WebLINX,
OpenApps, and TimeWarp.

- Repository: https://github.com/ServiceNow/BrowserGym
- Relevance:
  - Web-agent evaluation
  - Browser interaction
  - Multi-step tasks
  - Reproducible experiments
  - Benchmark comparison

## Dataset Selection Rationale

These resources cover complementary failure modes:

| Resource | Primary Focus |
|---|---|
| WebArena | Realistic multi-step web tasks |
| AgentDojo | Prompt injection and agent security |
| AgentBench | General agent evaluation |
| Mind2Web | Real-world web interaction |
| BrowserGym | Unified web-agent evaluation |

## Research Relevance

These datasets and benchmark environments can support experiments
investigating:

- Tool misuse
- Incorrect tool selection
- Error propagation
- State-tracking failures
- Long-horizon task failure
- Prompt injection
- Unsafe tool execution
- Lack of verification
- Agent robustness
- Multi-step planning failures

## Important Note

Dataset availability, task counts, benchmark versions, and evaluation
procedures can change. Researchers should consult the original
repository and paper before reporting experimental results.
