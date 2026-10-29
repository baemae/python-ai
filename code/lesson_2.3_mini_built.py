"""Lesson 2.3: Bakery bot that uses real facts and can switch personality."""

from langchain.chat_models import init_chat_model

config = {"model": "llama3.2", "temperature": 0.3, "max_messages": 6}

facts = {
    "name": "Sweet Crumbs",
    "city": "Lahore",
    "hours": "9 am to 10 pm",
    "prices": {"chocolate cake": 1500, "cupcake": 250, "brownie": 300},
}

personas = {
    "friendly": "warm and cheerful, uses simple words",
    "formal": "polite and professional, no jokes",
    "sales" : "excited, always suggests one extra item to buy",
}

# One config dictionary controls the model, so settings live in one place
llm = init_chat_model(config["model"], model_provider="ollama", temperature=config["temperature"])

# Facts go into the system message so the AI does not invent prices or hours
rules = (
    f"You are the assistant of {facts['name']} bakery in {facts['city']}. "
    f"Hours: {facts['hours']}. Prices in PKR: {facts['prices']}. "
    "Only use these facts. Answer in 2 short lines."
)
style = personas["friendly"]
messages = [{"role": "system", "content": f"{rules} Your style: {style}."}]

print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, bye")

while True:
    text = input("You: ").strip()

    if text.lower() == "bye":
        print("Bot: Goodbye!")
        break
    elif text.startswith("/persona "):
        name = text[9:].strip().lower()
        # .get with a default, so a wrong name keeps the bot working
        style = personas.get(name, personas["friendly"])
        messages[0]["content"] = f"{rules} Your style: {style}."
        print(f"Bot: Style changed to: {style}")
    elif text.startswith("/price "):
        item = text[7:].strip().lower()
        # Price questions are answered from the dictionary: free, instant, never wrong
        if item in facts["prices"]:
            print(f"Bot: {item.title()} costs {facts['prices'][item]} PKR.")
        else:
            print(f"Bot: Sorry, {item} is not on our menu.")
    else:
        messages.append({"role": "user", "content": text})
        messages = [messages[0]] + messages[1:][-config["max_messages"]:]
        response = llm.invoke(messages)
        answer = response.text
        messages.append({"role": "assistant", "content": answer})
        print(f"Bot: {answer}")