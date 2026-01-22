from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template("Tell a joke about {topic}")
print(prompt.format(topic="robots"))
