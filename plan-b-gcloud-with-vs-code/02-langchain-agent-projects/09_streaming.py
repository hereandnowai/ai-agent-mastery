from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatOpenAI()
for chunk in llm.stream("Write a 3-sentence poem about AI"):
    print(chunk.content, end="|", flush=True)
