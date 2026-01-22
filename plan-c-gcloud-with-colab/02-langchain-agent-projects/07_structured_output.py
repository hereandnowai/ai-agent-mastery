
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
class Joke(BaseModel):
    setup: str = Field(description="The setup")
    punchline: str = Field(description="The punchline")
llm = ChatOpenAI().with_structured_output(Joke)
print(llm.invoke("Tell me a funny joke"))
