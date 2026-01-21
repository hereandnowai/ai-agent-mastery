import autogen

# Autogen (Conversation-based)
# Configured to use gemma3:270m via Ollama
config_list = [
    {
        "model": "gemma3:270m",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama", # placeholder
    }
]

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"config_list": config_list},
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=2,
    code_execution_config=False,
)

user_proxy.initiate_chat(
    assistant,
    message="Tell me a 1-sentence joke about AI agents.",
)
