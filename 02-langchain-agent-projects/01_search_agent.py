from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools.tavily_search import TavilySearchResults
import os

# Set your API keys
# os.environ["OPENAI_API_KEY"] = "your-key"
# os.environ["TAVILY_API_KEY"] = "your-key"

def main():
    # 1. Define Tools
    search = TavilySearchResults()
    tools = [search]

    # 2. Configure LLM
    llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)

    # 3. Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/openai-tools-agent")

    # 4. Construct the Tool Calling Agent
    agent = create_openai_tools_agent(llm, tools, prompt)

    # 5. Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # 6. Run the agent
    query = "What is the current stock price of NVIDIA and who is the CEO?"
    agent_executor.invoke({"input": query})

if __name__ == "__main__":
    main()
