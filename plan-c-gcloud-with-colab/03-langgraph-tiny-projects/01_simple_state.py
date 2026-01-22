
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from typing import TypedDict
class State(TypedDict):
    count: int
state: State = {"count": 1}
print(state)
