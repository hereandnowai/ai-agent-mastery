from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
class Joke(BaseModel):
    setup: str = Field(description="The setup")
    punchline: str = Field(description="The punchline")
llm = ChatOpenAI().with_structured_output(Joke)
print(llm.invoke("Tell me a funny joke"))
