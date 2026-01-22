from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()
# Upgrade to 1b local model for better accuracy/less hallucination
llm = ChatOllama(model='gemma3:270m', temperature=0)
search = TavilySearch(max_results=5)

# Dynamic Query - change this variable to ask anything!
query = "Who is the founder of google?"

print(f"Agent is searching for: {query}...")
res = search.invoke(query)
context = "\n".join([r['content'] for r in res.get('results', [])])

prompt = f"Using this info: {context}\n\nQuestion: {query}\nAnswer:"
print(f"Final Answer: {llm.invoke(prompt).content.strip()}")