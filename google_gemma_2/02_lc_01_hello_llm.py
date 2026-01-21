import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemma2", google_api_key=os.getenv("GOOGLE_API_KEY"))
print(llm.invoke("Hello, who are you?").content)
