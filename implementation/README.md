# Implementation

Implementation guidance for building, testing, and evaluating reliable
chained tool-calling agents operating without human checkpoints.

## 1. Agent Execution Pipeline

A basic chained tool-calling system can be organized as:

User Task
    ↓
Task Understanding
    ↓
Planning
    ↓
Tool Selection
    ↓
Tool Input Validation
    ↓
Tool Execution
    ↓
Tool Output Validation
    ↓
State Update
    ↓
Next Action
    ↓
Verification
    ↓
Final Result

Each stage should be observable and independently testable.

## 2. Tool Input Validation

Before executing a tool, validate:

- Tool name
- Required arguments
- Argument types
- Argument ranges
- Authorization
- Resource permissions
- Whether the requested action matches the task

Invalid or suspicious tool calls should be rejected before execution.

## 3. Tool Output Validation

Tool results should not automatically be treated as trusted facts.

Recommended checks include:

- Schema validation
- Type validation
- Expected-value checks
- Source validation
- Consistency checks
- Error-status checks
- Detection of unexpected instructions in external content

This is particularly important when tool output becomes input to a
subsequent tool call.

## 4. Error Propagation Control

A chained agent can propagate an incorrect intermediate result through
later steps.

Recommended controls:

1. Validate each intermediate result.
2. Record the source of each result.
3. Separate tool output from agent instructions.
4. Stop execution when a critical validation fails.
5. Re-check important assumptions before irreversible actions.
6. Avoid silently replacing failed tool calls with invented results.

## 5. State Tracking

Maintain an explicit execution state containing information such as:

- Current task
- Completed actions
- Pending actions
- Tool calls
- Tool results
- Validation results
- Errors
- Retry count
- Approval status

Checkpointing can make long-running workflows recoverable and can support
human review, memory, debugging, and fault-tolerant execution.

## 6. Human Checkpoints

Sensitive actions should be interruptible before execution.

Examples include:

- Sending messages
- Deleting data
- Making purchases
- Changing permissions
- Executing destructive commands
- Publishing information
- Modifying important files

A human reviewer should be able to:

- Approve
- Reject
- Modify

Human-in-the-loop systems can pause execution, persist state, obtain a
decision, and then resume the workflow.

## 7. Guardrails

Guardrails can be placed at multiple boundaries:

### Input

Check whether the user's request is valid and within the permitted
task scope.

### Tool Input

Check tool arguments before execution.

### Tool Output

Check returned data before it becomes part of subsequent reasoning.

### Final Output

Check whether the final result satisfies task requirements and safety
constraints.

## 8. Prompt-Injection Defense

External content should be treated as untrusted data.

Potential sources include:

- Web pages
- Emails
- Documents
- Search results
- Tool responses
- Retrieved memory
- Database records

Recommended defenses include:

- Separate instructions from untrusted content.
- Validate tool calls against the original task.
- Restrict tool permissions.
- Use allowlists where appropriate.
- Require approval for high-impact actions.
- Detect suspicious instructions in external data.
- Stop or quarantine execution when an injection is detected.

## 9. Verification

Verification should occur throughout execution rather than only at the
end.

Useful verification points include:

- After planning
- Before a tool call
- After a tool result
- Before an irreversible action
- Before producing the final answer

A useful design principle is:

    Plan → Act → Observe → Verify → Continue

rather than:

    Plan → Act → Act → Act → Final Answer

## 10. Logging and Tracing

Record enough information to reconstruct an agent run.

Useful fields include:

- Timestamp
- Agent or workflow step
- Tool name
- Tool arguments
- Tool result status
- Validation result
- Error information
- Approval decision
- Retry count
- Final outcome

Tracing can help identify where a multi-step workflow first deviated
from the intended task.

## 11. Failure Recovery

When a tool call fails:

1. Record the failure.
2. Determine whether the error is transient or permanent.
3. Retry only when retrying is safe.
4. Validate the new result.
5. Avoid repeating destructive actions.
6. Escalate to a human when necessary.
7. Preserve the failed state for later analysis.

## 12. Testing Strategy

Test agents using controlled failure scenarios.

### Tool Failure

Return invalid, incomplete, delayed, or erroneous tool results.

### Planning Failure

Provide ambiguous or conflicting task requirements.

### State Failure

Modify or remove intermediate state.

### Prompt Injection

Place malicious instructions inside otherwise trusted-looking
external content.

### Permission Failure

Attempt actions outside the agent's permitted capabilities.

### Long-Horizon Failure

Evaluate whether small errors propagate through many chained actions.

## 13. Evaluation Metrics

Possible metrics include:

- Task success rate
- Tool-call accuracy
- Tool-selection accuracy
- Invalid tool-call rate
- Error recovery rate
- Error propagation rate
- Prompt-injection success rate
- Unsafe-action rate
- Verification coverage
- Human-intervention rate
- Average number of tool calls
- Task completion latency

## 14. Reference Implementations

Potential implementation frameworks include:

- OpenAI Agents SDK
- LangGraph
- LangChain
- Microsoft AutoGen
- Model Context Protocol (MCP)

These frameworks provide different mechanisms for tool execution,
workflow orchestration, state management, guardrails, interruptions,
and tracing.

## 15. Research Experiment Template

A reproducible experiment can use:

1. Define a multi-step task.
2. Define the available tools.
3. Define the expected tool sequence.
4. Introduce a controlled failure.
5. Run the agent without intervention.
6. Record all tool calls and intermediate states.
7. Measure whether the failure propagates.
8. Repeat with verification enabled.
9. Repeat with human checkpoints enabled.
10. Compare the outcomes.

## 16. Research Objective

The implementation resources in this directory support experiments
investigating:

- Tool misuse
- Incorrect tool selection
- Error propagation
- Hallucinated intermediate results
- Prompt injection
- Memory and state failures
- Planning failures
- Lack of verification
- Unsafe autonomous actions
- Lack of human checkpoints
- Multi-step task failure
