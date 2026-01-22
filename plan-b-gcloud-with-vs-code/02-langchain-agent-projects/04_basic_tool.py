from dotenv import load_dotenv
load_dotenv()
from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b
print(add.invoke({"a": 1, "b": 2}))
