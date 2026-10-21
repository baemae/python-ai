"""Clean a user's name and question before sending a prompt to AI.
this tool helps an AI agency prepare clear, measured questions that fit within a safe character limit.
"""

#strip will remove extra spaces, while title() formats the name for a greeting
user_name = input("Your name: ").strip().title()

# strip() removes surrounding spaces, and capitalize() standardizes the question.
question = input("Your question: ").strip().capitalize()

# Counting characters gives us a simple way to estimate the prompt's token usage.
character_count = len(question)
estimated_tokens = round(character_count / 4)

# lower() makes the keyword check work even when the user types different capitals.
mentions_python = "python" in question.lower()

# Stretch goal: replace an unwanted word before building the final prompt.
cleaned_question = question.replace("stupid", "***")

# Slicing limits the question so the prompt never includes more than 150 characters.
prompt = f"""You are a friendly Python tutor.
Greet {user_name} by name and answer in 3 short lines.
Question: {cleaned_question[:150]}"""

print("=" * 40)
print(f"Cleaned question: {question}")
print(f"Characters: {character_count}, about {estimated_tokens} tokens")
print(f"Mentions Python: {mentions_python}")
print("=" * 40)
print(prompt)

# This example rate demonstrates cost estimation; it is not a real model price.
example_price_per_1k_tokens = 0.50
estimated_cost = estimated_tokens / 1000 * example_price_per_1k_tokens
print(f"Estimated cost: {estimated_cost:.2f} PKR")
