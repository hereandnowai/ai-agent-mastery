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

There are several frameworks used to build these intelligent systems:

| Framework | Developer | Key Strength | Best For |
| :--- | :--- | :--- | :--- |
| **LangChain** | Harrison Chase | Modular components | Quick prototyping & integration |
| **LangGraph** | LangChain Team | Stateful cyclic graphs | Complex industry-grade workflows |
| **Crew AI** | João Moura | Role-playing agents | Collaborative multi-agent teams |
| **Auto Gen** | Microsoft | Conversation-based | Autonomous coding & research |
| **n8n** | n8n.io (Low-code) | Visual automation | Business workflows (No-code/Low-code) |

### 🚀 Which is the "Best"?
There is no single "best" framework. 
- Use **LangChain** for simple, linear pipelines.
- Use **LangGraph** when you need fine-grained control and cycles.
- Use **CrewAI** for high-level management tasks.
- Use **AutoGen** for self-correcting code generation.

---

## 📁 Folder Contents

### 🤖 Framework Chatbot Examples (Ollama/Gemma 3)
We have implemented 6 specialized chatbots using different industry frameworks, all powered by `gemma3:270m` served via Ollama:

1.  **01_autogen_chatbot.py**: Conversation-based multi-agent pattern from Microsoft.
2.  **02_crewai_chatbot.py**: Role-playing, hierarchy-based task execution.
3.  **03_openai_chatbot.py**: Simple SDK usage via Ollama's OpenAI-compatible layer.
4.  **04_google_adk_chatbot.py**: Raw API interaction style using HTTP requests.
5.  **05_langchain_chatbot.py**: Chain-based logic using LangChain Expression Language (LCEL).
6.  **06_langgraph_chatbot.py**: Stateful, graph-based autonomy.

---

### 📂 Legacy Examples
- `langchain_example.py`: A basic LangChain tool-calling agent.
- `langgraph_example.py`: A simple stateful graph agent.
- `crewai_example.py`: Introduction to CrewAI.
- `autogen_example.py`: Introduction to Microsoft AutoGen.
- `hello_agent.py`: Initial LLM connectivity test.
- `crewai_example.py`: A multi-agent "Manager/Worker" demonstration.
- `autogen_example.py`: A conversational coding agent example.

---
*Created by [HERE AND NOW AI](https://hereandnowai.com)*
