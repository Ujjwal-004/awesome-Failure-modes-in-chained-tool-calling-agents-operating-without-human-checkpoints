# Research References

Research papers related to chained tool-calling agents, agent reliability,
error propagation, prompt injection, tool use, security, memory, and
evaluation.

## 1. Tool Use and Agent Foundations

1. **Toolformer: Language Models Can Teach Themselves to Use Tools**
   - Authors: Timo Schick et al.
   - Year: 2023
   - Identifier: arXiv:2302.04761
   - Relevance: Self-supervised learning of tool use by language models.

2. **ReAct: Synergizing Reasoning and Acting in Language Models**
   - Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran,
     Karthik Narasimhan, Yuan Cao
   - Year: 2022
   - Identifier: arXiv:2210.03629
   - Relevance: Interleaves reasoning and external actions, providing a
     foundation for chained tool-calling agents.

3. **WebArena: A Realistic Web Environment for Building Autonomous Agents**
   - Authors: Shuyan Zhou et al.
   - Year: 2023
   - Identifier: arXiv:2307.13854
   - Relevance: Benchmark for autonomous agents performing multi-step tasks
     in realistic web environments.

4. **Reflexion: Language Agents with Verbal Reinforcement Learning**
   - Authors: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath,
     Karthik Narasimhan, Shunyu Yao
   - Year: 2023
   - Identifier: arXiv:2303.11366
   - Relevance: Uses verbal feedback and episodic memory to improve agent
     performance across repeated trials.

## 2. Agent Evaluation and Reliability

5. **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks
   and Defenses for LLM Agents**
   - Authors: Edoardo Debenedetti, Jie Zhang, Mislav Balunovic,
     Luca Beurer-Kellner, Marc Fischer, Florian Tramèr
   - Year: 2024
   - Venue: NeurIPS 2024
   - DOI: 10.52202/079017-2636
   - Relevance: Evaluates agents executing tools over untrusted data and
     demonstrates failures caused by prompt injection and task complexity.

6. **Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and
   Defenses in LLM-based Agents**
   - Authors: Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao,
     Zhenting Wang, Chenlu Zhan, Hongwei Wang, Yongfeng Zhang
   - Year: 2024
   - Identifier: arXiv:2410.02644
   - Relevance: Comprehensive benchmark covering attacks, defenses, tools,
     memory, and multiple agent scenarios.

7. **The Task Shield: Enforcing Task Alignment to Defend Against Indirect
   Prompt Injection in LLM Agents**
   - Authors: Feiran Jia, Tong Wu, Xin Qin, Anna Squicciarini
   - Year: 2025
   - Venue: ACL 2025
   - DOI: 10.18653/v1/2025.acl-long.1435
   - Relevance: Defense mechanism that verifies whether agent instructions
     and tool calls remain aligned with the user's task.

## 3. Security and Prompt Injection

8. **Not what you've signed up for: Compromising Real-World LLM-Integrated
   Applications with Indirect Prompt Injection**
   - Authors: Fabio Perez, Ian Ribeiro
   - Year: 2022
   - Identifier: arXiv:2211.09527
   - Relevance: Studies indirect prompt injection against applications
     integrating LLMs with external data and tools.

9. **Ignore Previous Prompt: Attack Techniques For Language Models**
   - Authors: Various researchers
   - Year: 2023
   - Relevance: Provides background on prompt injection and instruction
     hierarchy failures relevant to tool-using agents.

10. **Jailbroken: How Does LLM Safety Training Fail?**
    - Authors: Andy Wei et al.
    - Year: 2023
    - Relevance: Examines weaknesses in safety alignment that can contribute
      to unsafe agent behavior.

## 4. Autonomous Agents and Multi-Step Reasoning

11. **AutoGPT: An Autonomous GPT-4 Experiment**
    - Year: 2023
    - Relevance: Early autonomous-agent architecture illustrating recursive
      planning, tool use, and multi-step execution.

12. **Generative Agents: Interactive Simulacra of Human Behavior**
    - Authors: Joon Sung Park et al.
    - Year: 2023
    - Venue: UIST 2023
    - Relevance: Demonstrates memory, planning, reflection, and autonomous
      behavior in language-model-based agents.

13. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**
    - Authors: Shunyu Yao et al.
    - Year: 2023
    - Relevance: Explores structured search and evaluation of intermediate
      reasoning states.

## 5. Web and Tool-Calling Agents

15. **WebShop: Towards Scalable Real-World Web Interaction with Grounded
    Language Agents**
    - Authors: Shunyu Yao et al.
    - Year: 2022
    - Relevance: Evaluates language agents interacting with realistic web
      shopping environments.

16. **Mind2Web: Towards a Generalist Agent for the Web**
    - Authors: Xueguang Ma et al.
    - Year: 2023
    - Relevance: Studies general-purpose web agents and multi-step web
      interaction.

17. **BrowserGym: a Gym Environment for Web Task Automation**
    - Authors: Arthur Lefranc et al.
    - Year: 2024
    - Relevance: Provides an environment for evaluating web agents on
      realistic browser tasks.

## 6. Agent Planning, Memory and Error Propagation

18. **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**
    - Authors: Jason Wei et al.
    - Year: 2022
    - Relevance: Foundational work on multi-step reasoning and intermediate
      reasoning chains.

19. **Self-Refine: Iterative Refinement with Self-Feedback**
    - Authors: Aman Madaan et al.
    - Year: 2023
    - Relevance: Shows how iterative feedback can improve generated outputs
      and reduce errors.

20. **CRITIC: Large Language Models Can Self-Correct with Tool-Interactive
    Critiquing**
    - Authors: Zhibin Gou et al.
    - Year: 2024
    - Relevance: Uses external tools for critique and self-correction,
      directly relevant to verification in tool-using agents.

21. **AgentBench: Evaluating LLMs as Agents**
    - Authors: Xiao Liu et al.
    - Year: 2023
    - Relevance: Benchmark for evaluating LLM agents across multiple
      environments and task types.

## 7. Key Research Themes

The papers above are organized around the following failure modes:

- Tool misuse
- Incorrect tool selection
- Error propagation across chained steps
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

## Verification Note

The references in this file should be verified against their original
scholarly records before being cited as evidence in the final research paper.
DOI, arXiv identifier, publisher, conference, author, and year information
should be checked against the original source.
