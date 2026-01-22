from dotenv import load_dotenv
load_dotenv()
from langchain.chains import LLMMathChain
from langchain_google_genai import ChatGoogleGenerativeAI
math_chain = LLMMathChain.from_llm(ChatOpenAI())
print(math_chain.invoke("What is 123 * 456?"))
