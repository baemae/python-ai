"""Personal bot for the bakery Sweet Crumbs"""

from langchain.chat_models import init_chat_model

config = {
     "model": "llama3.2",
    "provider": "ollama",
    "temperature": 0.2,
    "max_messages": 8,
}

# a fact dictionary for the business
facts = {
    "name": "Sweet Crumbs",
    "city": "lahore",
    "hours": "9am to 9pm, every day",
    "delivery": "free delivery above 2000 PKR",
    "phone": "0300-0000000",
    "prices": {"cupcake": 250, "brownie": 300, "cake": 1800},
}

# creating a persona dictionary for three different styles
personas = {
    "friendly": "warm and cheerful, uses simple words",
    "formal" : "polite and professioanl, no slang",
    "sales": "excited, always suggests one extra item to buy ",
}

DEFAULT_PERSONA = "friendly"

def build_system_message(style):
    """Return the system prompt built from the current facts and style."""
    price_lines = ",".join(
        f"{item} {price} PKR" for item, price in facts["prices"].items()
    )
    # Why: telling the AI to ONLY use these facts (and to admit when it
    # doesn't know) is what stops it from inventing prices or products
    return(
         f"You are the assistant for {facts['name']} in {facts['city']}. "
        f"Opening hours: {facts['hours']}. Delivery: {facts['delivery']}. "
        f"Phone: {facts['phone']}. Prices: {price_lines}. "
        "Only use these facts. If something is not listed here, say you "
        "do not know and never invent products or prices. "
        f"Speak in this style: {style}. Keep answers to 3 lines."
    )

llm = init_chat_model(
    config["model"],
    model_provider=config["provider"],
    temperature = config["temperature"],
)

current_persona = DEFAULT_PERSONA
messages = [
    {"role": "system", "content": build_system_message(personas[current_persona])}
]

print("Bot ready. Commands: /persona friendly|formal|sales, /price <item>, /add <item> <price>, bye")

while True:
    text =  input("You: ").strip()
    parts = text.split()
    command = parts[0].lower() if parts else ""
    
    if text.lower() == "bye":
        break

    elif text == "":
        print("bot: Aske me Anything")

    elif command == "/persona":
        name = parts[1].lower() if len(parts) >1 else ""
         # Why: .get() with a default means a wrong name (like "pirate")
        # falls back to the default style instead of crashing with KeyError.
    elif command == "/price":
        # .lower() so "Cupcake", "CUPCAKE" and "cupcake" all match.
        item = " ".join(parts[1:]).lower()
        price = facts["prices"].get(item)
        if price is None:
            print(f"Bot: Sorry, {item or 'that'} is not on our menu.")
        else:
            print(f"Bot: {item.capitalize()} costs {price} PKR.")
 
    elif command == "/add":
        # Stretch: /add <item> <price>. The item can be several words,
        # the price is always the last word.
        try:
            item = " ".join(parts[1:-1]).lower()
            price = int(parts[-1])
            if not item:
                raise ValueError
        except ValueError:
            print("Bot: Use it like this: /add chocolate cake 2000")
            continue
        facts["prices"][item] = price
        # Why: the system message was built from the OLD facts, so we must
        # rebuild it, otherwise the AI would not know about the new item.
        messages[0]["content"] = build_system_message(personas[current_persona])
        print(f"Bot: Added {item} at {price} PKR.")
 
    else:
        messages.append({"role": "user", "content": text})
        response = llm.invoke(messages)
        messages.append({"role": "assistant", "content": response.content})
        # Keep the system message plus only the last N messages.
        messages = [messages[0]] + messages[1:][-config["max_messages"]:]
        print(f"Bot: {response.content}")