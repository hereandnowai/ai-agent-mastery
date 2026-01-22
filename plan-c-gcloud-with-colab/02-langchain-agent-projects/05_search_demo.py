import os
try:
    from google.colab import userdata
    os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
    os.environ["TAVILY_API_KEY"] = userdata.get("TAVILY_API_KEY")
except ImportError:
    # Fallback for local testing
    from dotenv import load_dotenv
    load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Initialize the model
llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it")

# Initialize the search tool
search = TavilySearchResults(max_results=5)

# 1. Search for the CEO
query = 'CEO "HERE AND NOW AI"'
search_results = search.invoke(query)

# 2. Filter results
filtered_results = []
for res in search_results:
    content_lower = res['content'].lower()
    if "here and now ai" in content_lower:
        filtered_results.append(res['content'])

context = "\n---\n".join(filtered_results) if filtered_results else "\n---\n".join([r['content'] for r in search_results])

# 3. Use the LLM to extract the final answer
prompt = f"""
Answer the question based ONLY on the provided snippets.
Question: Who is the CEO of HERE AND NOW AI?

Snippets:
{context}

Answer:"""

answer = llm.invoke(prompt)

print(f"Query: {query}")
print(f"Final Answer: {answer.content.strip()}")
