
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
messages = [HumanMessage(content="Hi"), AIMessage(content="Hello!")]
print(ChatOpenAI().invoke(messages + [HumanMessage(content="How are you?")]).content)
