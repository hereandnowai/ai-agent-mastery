# Section 1: Introduction to AI Agents

Welcome to the start of your journey. In this module, we explore the fundamental concepts of Agents, AI Agents, and the modern ecosystem used to build them.

## 🕵️ What is an Agent?
In general terms, an **Agent** is an entity capable of acting on behalf of someone or something else. It perceives its environment, takes actions to achieve a goal, and can operate autonomously to a certain degree.

## 🤖 What is an AI Agent?
An **AI Agent** is a software system that uses a Large Language Model (LLM) as its "brain" or reasoning engine. Unlike traditional software that follows a fixed script (if-then-else), an AI Agent can:
1.  **Reason:** Analyze a goal and break it down.
2.  **Plan:** Decide which steps to take first.
3.  **Act:** Use external tools (Search, APIs, Code) to get tasks done.
4.  **Reflect:** Check its own work and correct errors.

---

## 🏗 Types of AI Agents

1.  **Simple Reflex Agents:** Act based on current perceptions (Short-term memory).
2.  **Goal-Based Agents:** Work towards a specific defined objective.
3.  **Utility-Based Agents:** Optimize for the best possible outcome (Efficiency).
4.  **Learning Agents:** Improve their performance over time through feedback.

---

## 🛠 Framework Ecosystem

This module focuses on the two most industry-relevant frameworks for building AI agents:

| Framework | Developer | Key Strength | Best For |
| :--- | :--- | :--- | :--- |
| **LangChain** | Harrison Chase | Modular components | Quick prototyping & integration |
| **LangGraph** | LangChain Team | Stateful cyclic graphs | Complex industry-grade workflows |

### 🚀 Choosing the Right Tool
- Use **LangChain** for simple, linear pipelines and task automation.
- Use **LangGraph** when you need fine-grained control, state persistence, and complex decision cycles.

---

## 📁 Folder Contents

### 🤖 Chatbot Examples (Ollama/Gemma 3)
We have implemented core chatbots using **LangChain** and **LangGraph**, powered by `gemma3:270m` served via Ollama:

1.  **05_langchain_chatbot.py**: Chain-based logic using LangChain Expression Language (LCEL).
2.  **06_langgraph_chatbot.py**: Stateful, graph-based autonomy.

---

### 📂 Fundamental Examples
- `langchain_example.py`: A basic LangChain tool-calling agent.
- `langgraph_example.py`: A simple stateful graph agent.
- `hello_agent.py`: Initial LLM connectivity test.

---
*Created by [HERE AND NOW AI](https://hereandnowai.com)*
