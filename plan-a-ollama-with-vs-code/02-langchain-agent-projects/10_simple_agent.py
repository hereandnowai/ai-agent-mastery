from langchain_ollama import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain.agents import load_tools
llm = ChatOllama(model="gemma3:270m")
agent = initialize_agent(load_tools(["llm-math"], llm=llm), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("2+2 is?")
