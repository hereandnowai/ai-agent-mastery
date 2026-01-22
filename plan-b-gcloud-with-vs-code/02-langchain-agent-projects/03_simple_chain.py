from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
chain = ChatPromptTemplate.from_template("{t}") | ChatOpenAI()
print(chain.invoke({"t": "Hi"}).content)
