from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemma-3-27b-it")
print(llm.invoke("Hello, who are you?").content)
