import os
import operator
from dotenv import load_dotenv
from typing import Annotated, TypedDict, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END

load_dotenv()

class TeamState(TypedDict):
    task: str
    reports: Annotated[List[str], operator.add]
    next_step: str

llm = ChatGoogleGenerativeAI(model="gemma2", google_api_key=os.getenv("GOOGLE_API_KEY"))

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
builder.add_conditional_edges("analyst", lambda x: "researcher") # Simplified for demo
builder.add_edge("researcher", END)

graph = builder.compile()
print("Google Gemma 2 Multi-Agent Ready")
# graph.invoke({"task": "AI Trends", "reports": []})
