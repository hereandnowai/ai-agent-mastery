
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatOpenAI()
for chunk in llm.stream("Write a 3-sentence poem about AI"):
    print(chunk.content, end="|", flush=True)
