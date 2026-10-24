
"""Route AI requests to models based on task type and estimated cost.

This tool helps a company reduce AI costs while keeping private data
on a local model and sending coding tasks to a stronger cloud model.
"""

# Cleaning the input makes choices like " Code " work correctly.
task = input("Task (code / private / chat): ").strip().lower()

# int() converts the token count from text into a number for comparisons and maths.
tokens = int(input("Estimated tokens: "))

if task == "private":
    model = "llama3.2 (local, Ollama)"
    price = 0
elif task == "code":
    model = "claude (cloud, strong at code)"
    price = 0.8
else:
    model = "gemma3 (cheap model)"
    price = 0.1

# Warn about long requests so users can consider reducing unnecessary tokens.
if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# The example price is per 1,000 tokens and is for the assignment, not a live quote.
cost = (tokens / 1000) * price

print(f"Chosen model: {model}")
print(f"Estimated cost: {cost:.2f} PKR")

# Stretch goal: warn free users when their request exceeds 2,000 tokens.
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

if paid_user == "no" and tokens > 2000:
    print("Upgrade to send long requests.")
