from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
messages = [HumanMessage(content="Hi"), AIMessage(content="Hello!")]
print(ChatOpenAI().invoke(messages + [HumanMessage(content="How are you?")]).content)
