import autogen
config = {"config_list": [{"model": "gpt-4o", "api_key": "YOUR_KEY"}]}
user = autogen.UserProxyAgent("user", code_execution_config=False)
assistant = autogen.AssistantAgent("assistant", llm_config=config)
user.initiate_chat(assistant, message="Write a poem about AI.")
