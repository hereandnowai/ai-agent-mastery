
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain_community.tools.tavily_search import TavilySearchResults
search = TavilySearchResults(max_results=1)
print(search.invoke("Who is the CEO of HERE AND NOW AI?"))
