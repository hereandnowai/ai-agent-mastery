from crewai import Agent, Task, Crew
manager = Agent(role="Manager", goal="Analyze tasks", backsplash="Expert")
task = Task(description="Write a hello world", agent=manager)
crew = Crew(agents=[manager], tasks=[task])
print(crew.kickoff())
