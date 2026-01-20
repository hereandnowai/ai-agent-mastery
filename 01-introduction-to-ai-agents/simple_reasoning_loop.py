"""
Simple Reasoning Loop (ReAct) Implementation
This script demonstrates the logic of an agent without using LangChain or LangGraph.
It shows how an LLM can 'think' and then 'act'.
"""

def simple_tool(query):
    """A mock tool that returns data based on a query."""
    if "weather" in query.lower():
        return "The weather is 25°C and sunny."
    return "I don't have information on that."

def mock_llm_call(prompt):
    """
    Mocks an LLM response. 
    In a real scenario, this would call OpenAI/Anthropic/Gemini.
    """
    if "THOUGHT:" not in prompt:
        return "THOUGHT: The user wants to know about the weather. I should use the weather tool.\nACTION: weather in London"
    else:
        return "FINAL ANSWER: The weather in London is 25°C and sunny."

def run_agent(user_input):
    print(f"User: {user_input}")
    
    # Step 1: LLM generates Thought and Action
    response = mock_llm_call(user_input)
    print(f"Agent {response}")
    
    if "ACTION:" in response:
        # Extract action
        action = response.split("ACTION:")[1].strip()
        print(f"Executing Tool: {action}")
        
        # Step 2: Execute Tool (Observation)
        observation = simple_tool(action)
        print(f"Observation: {observation}")
        
        # Step 3: LLM generates Final Answer based on Observation
        final_prompt = f"{user_input}\n{response}\nOBSERVATION: {observation}"
        final_response = mock_llm_call(final_prompt)
        print(f"Agent {final_response}")

if __name__ == "__main__":
    run_agent("What is the weather like?")
