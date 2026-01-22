
from google.colab import userdata
import os
os.environ["GOOGLE_API_KEY"] = userdata.get("GOOGLE_API_KEY")
from typing import TypedDict, Annotated
import operator
class State(TypedDict):
    logs: Annotated[list, operator.add]
builder = StateGraph(State)
builder.add_node("a", lambda s: {"logs": ["hi"]})
builder.set_entry_point("a")
builder.set_finish_point("a")
print(builder.compile().invoke({"logs": []}))
