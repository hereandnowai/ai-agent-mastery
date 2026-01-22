from typing import TypedDict
class State(TypedDict):
    count: int
state: State = {"count": 1}
print(state)
