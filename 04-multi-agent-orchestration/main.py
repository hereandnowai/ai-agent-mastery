"""
Capstone Project: Global Market Research Swarm
A multi-agent system built with LangGraph.
"""

from typing import Annotated, List, Tuple, Union
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import END, StateGraph

# 1. State Definition
class SwarmState(TypedDict):
    messages: Annotated[List[BaseMessage], "The conversation history"]
    team_lead_plan: str
    data_collected: List[str]
    report_ready: bool

# 2. Define Nodes (Agent Logic)
def supervisor_node(state: SwarmState):
    print("--- SUPERVISOR ---")
    return {"messages": ["Supervisor planned the next steps."]}

def researcher_node(state: SwarmState):
    print("--- RESEARCHER ---")
    return {"data_collected": ["Found Apple Q3 earnings data."]}

def analyst_node(state: SwarmState):
    print("--- ANALYST ---")
    return {"messages": ["Analyzed the earnings data. Sentiment is positive."]}

def writer_node(state: SwarmState):
    print("--- WRITER ---")
    return {"report_ready": True}

# 3. Graph Construction
workflow = StateGraph(SwarmState)

workflow.add_node("supervisor", supervisor_node)
workflow.add_node("researcher", researcher_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("writer", writer_node)

workflow.set_entry_point("supervisor")

# Define transitions
workflow.add_edge("supervisor", "researcher")
workflow.add_edge("researcher", "analyst")
workflow.add_edge("analyst", "writer")
workflow.add_edge("writer", END)

# 4. Compile and Run
app = workflow.compile()

if __name__ == "__main__":
    print("Starting Global Market Research Swarm...")
    initial_state = {
        "messages": [],
        "team_lead_plan": "",
        "data_collected": [],
        "report_ready": False
    }
    for output in app.stream(initial_state):
        print(output)
