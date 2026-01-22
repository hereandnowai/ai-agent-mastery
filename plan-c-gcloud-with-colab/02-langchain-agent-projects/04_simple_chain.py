
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
chain = ChatPromptTemplate.from_template("{t}") | ChatOpenAI()
print(chain.invoke({"t": "Hi"}).content)
