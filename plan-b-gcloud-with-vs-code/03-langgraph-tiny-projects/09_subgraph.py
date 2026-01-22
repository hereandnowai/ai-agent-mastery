from dotenv import load_dotenv
load_dotenv()
from langgraph.graph import StateGraph
sub = StateGraph(dict)
sub.add_node("s", lambda s: {"x": 1})
sub.set_entry_point("s")
sub.set_finish_point("s")
main = StateGraph(dict)
main.add_node("sub", sub.compile())
main.set_entry_point("sub")
main.set_finish_point("sub")
print(main.compile().invoke({}))
