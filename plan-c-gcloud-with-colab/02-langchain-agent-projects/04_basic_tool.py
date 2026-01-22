
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from langchain_core.tools import tool
@tool
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b
print(add.invoke({"a": 1, "b": 2}))
