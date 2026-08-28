# Tools and Frameworks

Tools, frameworks, and engineering resources relevant to building,
testing, evaluating, monitoring, and securing chained tool-calling agents.

## 1. OpenAI Agents SDK

The OpenAI Agents SDK provides primitives for building agents with
instructions, tools, handoffs, guardrails, sessions, human-in-the-loop
mechanisms, and tracing.

- Documentation: https://openai.github.io/openai-agents-python/
- Tools: https://openai.github.io/openai-agents-python/tools/
- Guardrails: https://openai.github.io/openai-agents-python/guardrails/

### Research Relevance

Useful for studying:

- Chained tool execution
- Tool selection
- Tool input/output validation
- Guardrails
- Human approval
- Agent handoffs
- Tracing and debugging
- Persistent agent sessions

The SDK documentation describes tool guardrails that can validate or
block custom function-tool calls before and after execution. It also
supports human approval for tools and tracing for agent workflows.

## 2. LangChain

LangChain is a framework for developing applications and agents that
use language models together with tools and external resources.

- Documentation: https://python.langchain.com/
- Relevance:
  - Tool calling
  - Agent orchestration
  - Multi-step workflows
  - Tool integration
  - State and memory

## 3. LlamaIndex

LlamaIndex provides components for building LLM applications and agents
that interact with external data and tools.

- Documentation: https://docs.llamaindex.ai/
- Relevance:
  - Agent workflows
  - Tool integration
  - Retrieval
  - Data access
  - Multi-step agent execution

## 4. Microsoft AutoGen

AutoGen is a framework for building applications involving multiple
agents and tool-enabled workflows.

- Documentation: https://microsoft.github.io/autogen/
- Relevance:
  - Multi-agent orchestration
  - Tool use
  - Agent communication
  - Workflow design
  - Autonomous execution

## 5. Model Context Protocol (MCP)

MCP provides a standardized way for AI applications to connect models
with external tools, resources, and services.

- Specification: https://modelcontextprotocol.io/
- Relevance:
  - Standardized tool access
  - External service integration
  - Tool discovery
  - Tool authorization and security

## 6. Browser Automation and Web-Agent Tools

Browser automation environments are important when evaluating agents
that interact with websites and other browser-based applications.

Relevant resources include:

- BrowserGym
- Playwright
- WebArena
- Mind2Web

These resources support research into:

- Browser actions
- State tracking
- Multi-step web tasks
- Navigation failures
- Incorrect actions
- Long-horizon execution

## 7. Security and Guardrail Tools

Security mechanisms are particularly important for chained tool-calling
agents because an unsafe intermediate result can influence later tool
calls.

Relevant mechanisms include:

- Input validation
- Output validation
- Tool-level guardrails
- Human approval
- Permission boundaries
- Tool allowlists
- Execution limits
- Prompt-injection detection
- Logging and tracing

## 8. Monitoring and Evaluation

Agent monitoring and evaluation tools can be used to inspect execution
traces and identify failures across multiple steps.

Important capabilities include:

- Tool-call logging
- Execution tracing
- Error tracking
- Latency measurement
- Failure classification
- Intermediate-state inspection
- Reproducible evaluation

## Tool Selection Principles

Tools used in research experiments should be evaluated according to:

1. Whether tool inputs are validated.
2. Whether tool outputs can be checked.
3. Whether execution can be interrupted.
4. Whether human approval can be required.
5. Whether tool calls are logged.
6. Whether failures can be reproduced.
7. Whether permissions can be restricted.
8. Whether untrusted external content is isolated from agent instructions.

## Research Relevance

The tools and frameworks in this directory support investigation of:

- Tool misuse
- Incorrect tool selection
- Error propagation
- Prompt injection
- Unsafe tool execution
- State-tracking failures
- Lack of verification
- Missing human checkpoints
- Agent security
- Multi-step task failure
- Monitoring and debugging
