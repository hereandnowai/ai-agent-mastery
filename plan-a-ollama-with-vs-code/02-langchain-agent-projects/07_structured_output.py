from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
class Joke(BaseModel):
    setup: str = Field(description="The setup")
    punchline: str = Field(description="The punchline")
llm = ChatOllama(model="gemma3:270m").with_structured_output(Joke)
print(llm.invoke("Tell me a funny joke"))
