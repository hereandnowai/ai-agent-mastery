from dotenv import load_dotenv
load_dotenv()
import operator
from typing import Annotated, TypedDict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END

class TeamState(TypedDict):
    task: str
    reports: Annotated[List[str], operator.add]
    next_step: str

llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it")

def analyst(state: TeamState):
    res = llm.invoke(f"Analyze this: {state['task']}")
    return {"reports": [f"Analysis: {res.content}"], "next_step": "researcher"}

def researcher(state: TeamState):
    res = llm.invoke(f"Research details for: {state['task']}")
    return {"reports": [f"Research: {res.content}"], "next_step": "end"}

builder = StateGraph(TeamState)
builder.add_node("analyst", analyst)
builder.add_node("researcher", researcher)
builder.add_edge(START, "analyst")
builder.add_conditional_edges("analyst", lambda x: x["next_step"])
builder.add_conditional_edges("researcher", lambda x: "end" if x["next_step"] == "end" else "analyst", {"end": END, "analyst": "analyst"})

graph = builder.compile()
print("Industry Grade Multi-Agent System Ready")
# graph.invoke({"task": "AI Market Trends", "reports": []})
