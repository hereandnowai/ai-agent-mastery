
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain.chains import LLMMathChain
from langchain_google_genai import ChatGoogleGenerativeAI
math_chain = LLMMathChain.from_llm(ChatOpenAI())
print(math_chain.invoke("What is 123 * 456?"))
