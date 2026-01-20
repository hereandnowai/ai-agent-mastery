from langchain_openai import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
llm = ChatOpenAI(model="gpt-4o")
agent = initialize_agent(load_tools(["llm-math"], llm=llm), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)
print(agent.run("What is 15% of 200?"))
