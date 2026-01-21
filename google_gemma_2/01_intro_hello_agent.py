import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
# google gemma 2
llm = ChatGoogleGenerativeAI(model="gemma2", google_api_key=os.getenv("GOOGLE_API_KEY"))
print(llm.invoke("Reasoning loop active. Hello!").content)
