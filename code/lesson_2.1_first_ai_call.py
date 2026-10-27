from langchain.chat_models import init_chat_model

llm = init_chat_model("llama3.2", model_provider="ollama")

response = llm.invoke([{"role": "user", "content": "Explain Python in 2 lines for beginner"}])

print(response.text)

print(response.response_metadata["model"])          # which model answered
print(response.usage_metadata["input_tokens"])      # tokens in your prompt
print(response.usage_metadata["output_tokens"])     # tokens in the answer
print(response.response_metadata["total_duration"]) # time in nanoseconds


#turn nanosec into seconds
seconds = response.response_metadata["total_duration"] / 1_000_000_000
total_tokens = response.usage_metadata["total_tokens"]
print(f"{total_tokens} tokens in {seconds:.1f} seconds")