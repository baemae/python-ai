"""Lesson 2.4: Bot battle: rules vs AI on the same test questions."""

from langchain.chat_models import init_chat_model

llm = init_chat_model("llama3.2", model_provider="ollama")

questions = [
    "What are your hours?",
    "How much is a cupcake?",
    "Do you have sugar-free options?",
    "Can I order a cake for 20 people?",
]

rule_misses = 0

for q in questions:
    text = q.lower()
    if "hour" in text:
        rule_answer = "We are open 9 am to 10 pm."
    elif "how much" in text or "price" in text:
        rule_answer = "Cupcakes are 250 PKR."
    else:
        rule_answer = "(no rule)"
        rule_misses += 1

    response = llm.invoke([
        {"role": "system", "content": "You are a bakery assistant. Hours 9 am to 10 pm. Cupcake 250 PKR. Answer in 1 line."},
        {"role": "user", "content": q},
    ])

    print(f"Q: {q}")
    print(f"   Rules: {rule_answer}")
    print(f"   AI:    {response.text.strip()}")

print(f"Rules could not answer {rule_misses} of {len(questions)} questions.")