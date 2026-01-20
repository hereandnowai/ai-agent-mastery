# Section 1: Introduction to AI Agents

Welcome to the start of your journey. In this module, we will define what AI agents are, how they differ from standard LLM applications, and build our first "autonomous" loop.

## 📝 What is an AI Agent?

An **AI Agent** is a system that uses a Large Language Model (LLM) as its reasoning engine to:
1.  **Reason** about a goal.
2.  **Plan** a sequence of steps.
3.  **Execute** actions using **Tools** (search, code execution, database access).
4.  **Observe** the outcome and adjust its plan.

### The Agentic Loop (ReAct)
The most common pattern is **Reason + Act (ReAct)**.
- **Input:** A complex user query.
- **Thought:** LLM thinks about what to do.
- **Action:** LLM chooses a tool and provides input.
- **Observation:** Result of the tool.
- **Loop:** Repeat until the final answer is found.

## 📁 Folder Contents

- `concepts.md`: Deep dive into Agent architectures (Agent, Chains, Tools, Memory).
- `simple_reasoning_loop.py`: A manual implementation of a ReAct loop without using any framework.
- `basic_tool_calling.py`: How to teach an LLM to use a mathematical tool.
- `demonstration_project.py`: A mini-project showing a "Personal Research Assistant" agent.

---

### Real-World Example
Imagine an agent that helps you plan a trip.
1. It searches for flights (Action).
2. It looks at the prices and decides they are too high (Reasoning).
3. It searches for alternative dates (New Action).
4. It books the best option (Final Action).

---
*Created by [HERE AND NOW AI](https://hereandnowai.com)*
