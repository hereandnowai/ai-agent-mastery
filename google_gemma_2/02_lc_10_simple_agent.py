import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents import load_tools

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemma2", google_api_key=os.getenv("GOOGLE_API_KEY"))
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("2+2 is?")
