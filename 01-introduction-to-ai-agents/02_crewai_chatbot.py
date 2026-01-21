from crewai import Agent, Task, Crew, Process

# CrewAI (Hierarchy-based)
# Using gemma3:270m via Ollama
# CrewAI can use model strings like 'ollama/model_name'
llm = "ollama/gemma3:270m"

chatbot_agent = Agent(
    role="Friendly AI",
    goal="Provide helpful answers",
    backstory="You are a lightweight model running locally.",
    llm=llm
)

task = Task(
    description="Say hello to the students of Sairam SIT.",
    agent=chatbot_agent,
    expected_output="A friendly greeting."
)

crew = Crew(
    agents=[chatbot_agent],
    tasks=[task],
    process=Process.sequential
)

print(crew.kickoff())
