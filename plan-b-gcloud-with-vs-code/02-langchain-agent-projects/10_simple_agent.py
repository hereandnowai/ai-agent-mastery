from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain.agents import load_tools
llm = ChatOpenAI()
agent = initialize_agent(load_tools(["llm-math"], llm=llm), llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("2+2 is?")
