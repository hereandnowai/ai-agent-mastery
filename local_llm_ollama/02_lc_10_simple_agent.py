from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain.agents import load_tools

llm = ChatOllama(model="ministral")
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("2+2 is?")
