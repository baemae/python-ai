
"""Create an AI model profile card and estimate chat costs.

This tool helps a client understand an AI model's basic details
and estimate the cost of using it for chats.
"""

# These variables use four different data types to describe the model.
model_name = "llama3.2"
context_window = 128000
price_per_1k_tokens = 0.5  # Example price in PKR, not an actual Ollama fee.
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# int() converts the user's input from text into a number for calculation.
tokens_per_chat = int(input("Tokens per chat: "))

# Dividing by 1000 matches the price's per-1,000-token unit.
estimated_cost = round((tokens_per_chat / 1000) * price_per_1k_tokens, 2)

print(f"Estimated cost: {estimated_cost} PKR")

# Stretch goal: estimate the cost of 30 days of chats.
chats_per_day = int(input("Chats per day: "))
monthly_cost = round(estimated_cost * chats_per_day * 30, 2)

print(f"Estimated monthly cost (30 days): {monthly_cost} PKR")
