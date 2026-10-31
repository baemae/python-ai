"""Module 2, Checkpoint 1 Project: AI Content Studio for Sweet Crumbs bakery.

A command-line studio for a local bakery in Lahore. It writes a description
for every menu item in one batch, streams social media posts in a chosen
tone, answers prices straight from a dictionary (no AI), and chats with
customers using memory and only real facts. When you type bye it prints a
session report of everything the AI did and what it cost.
Commands: /menu, /post <tone>, /price <item>, /reset, bye.
"""

import time
from langchain.chat_models import init_chat_model
# Why: one config dictionary means the model, temperatures and memory size
# are changed in one place instead of being hunted down in the code.
config = {
    "model": "llama3.2",
    "provider": "ollama",
    "precise_temp": 0.2,
    "creative_temp": 0.8,
    "max_messages": 8,
}
# Swap these for your own business if it is not a bakery.
facts = {
    "name": "Sweet Crumbs",
    "city": "Lahore",
    "hours": "9 am to 10 pm, every day",
    "delivery": "200 PKR, free for orders from 3,000 PKR",
    "phone": "0300-0000000",
    "prices": {
        "chocolate cake": 1500,
        "cupcake": 250,
        "brownie": 300,
        "mango tart": 0,  # 0 means "coming soon"
    },
}
tones = {
    "fun": "playful and full of energy, short sentences",
    "premium": "elegant and calm, focused on quality",
    "urgent": "exciting and time-limited, makes people act today",
}
default_tone = "fun"
# Why: two models for two jobs. Marketing text should be varied (creative),
# but customer answers must stick to the facts (precise, low temperature).
precise = init_chat_model(
    config["model"],
    model_provider=config["provider"],
    temperature=config["precise_temp"],
)
creative = init_chat_model(
    config["model"],
    model_provider=config["provider"],
    temperature=config["creative_temp"],
)
# Turn the nested prices dictionary into text the AI can read.
price_text = ""
for item, price in facts["prices"].items():
    if price == 0:
        price_text += f"{item}: coming soon (no price yet). "
    else:
        price_text += f"{item}: {price:,} PKR. "

facts_text = (
    f"Business: {facts['name']}, a bakery in {facts['city']}. "
    f"Opening hours: {facts['hours']}. Delivery: {facts['delivery']}. "
    f"Phone: {facts['phone']}. Prices: {price_text}"
)

# Why: telling the AI to ONLY use these facts, and to admit when it does not
# know, is what stops it from inventing prices like ChatGPT did for the owner.
system_text = (
    f"You are the customer assistant for {facts['name']}. {facts_text}"
    "Only use these facts. If something is not listed, say you do not know "
    "and never invent products or prices. Keep answers to 2 or 3 lines."
)
messages = [{"role": "system", "content": system_text}]
# Accumulators start at 0 BEFORE the loop so every command adds to the same totals.
total_tokens = 0
total_seconds = 0.0
chat_answers = 0
menu_descriptions = 0
posts = 0
price_answers = 0

print("=" * 50)
print(f"   {facts['name']} AI Content Studio")
print("=" * 50)
print(f"Commands: /menu, /post {'|'.join(tones)}, /price <item>, /reset, bye")

while True:
    text = input("You: ").strip()
    parts = text.split()
    command = parts[0].lower() if parts else ""

    if text == "":
        print("Studio: Please type a command or a question.")

    elif text.lower() == "bye":
        print("Studio: Goodbye!")
        break

    elif command == "/menu":
        results = []
        for name, price in facts["prices"].items():
            # Why: price 0 means "not for sale yet", so we skip it BEFORE
            # calling the AI. No call means no tokens and no cost.
            if price == 0:
                print(f"Studio: Skipping {name} (coming soon)")
                continue

            start = time.perf_counter()
            response = creative.invoke(
                [
                    {
                        "role": "system",
                        "content": (
                            f"You write menu descriptions for {facts['name']}, "
                            f"a bakery in {facts['city']}. "
                            "Reply with exactly one sentence and nothing else."
                        ),
                    },
                    {"role": "user", "content": f"Describe this item: {name}"},
                ]
            )
            total_seconds += time.perf_counter() - start
            total_tokens += response.usage_metadata["total_tokens"]
            menu_descriptions += 1
            results.append({"item": name, "price": price, "text": response.text.strip()})

        print("-" * 50)
        for number, entry in enumerate(results, start=1):
            print(f"{number}. {entry['item'].title()} ({entry['price']:,} PKR)")
            print(f"   {entry['text']}")
        print("-" * 50)

    elif command == "/post":
        tone_name = parts[1].lower() if len(parts) > 1 else ""
        # Why: .get() with a default means a wrong tone (like "pirate")
        # still works with the default style instead of crashing with KeyError.
        tone_style = tones.get(tone_name, tones[default_tone])

        print(f"Studio ({tone_style}):")
        start = time.perf_counter()
        full_message = None
        for chunk in creative.stream(
            [
                {
                    "role": "system",
                    "content": (
                        f"You write Instagram posts for {facts['name']}. {facts_text}"
                        f"Only use these facts. Tone: {tone_style}. "
                        "Write one short post of 3 or 4 lines about one product."
                    ),
                },
                {"role": "user", "content": "Write the post."},
            ]
        ):
            print(chunk.text, end="", flush=True)  # print each piece as it arrives
            # Chunks can be added together; the last one carries the token counts.
            full_message = chunk if full_message is None else full_message + chunk
        print()
        total_seconds += time.perf_counter() - start
        total_tokens += full_message.usage_metadata["total_tokens"]
        posts += 1

    elif command == "/price":
        # .lower() so "CUPCAKE", "Cupcake" and "cupcake" all match the keys.
        item = " ".join(parts[1:]).lower()
        price = facts["prices"].get(item)
        price_answers += 1  # answered from the dictionary: no AI, no tokens
        if price is None:
            print(f"Studio: Sorry, {item or 'that'} is not on our menu.")
        elif price == 0:
            print(f"Studio: {item.title()} is coming soon.")
        else:
            print(f"Studio: {item.title()} costs {price:,} PKR.")

    elif command == "/reset":
        # Why: keep messages[0] so the chat is forgotten but the rules
        # (only use these facts) stay in place.
        messages = [messages[0]]
        print("Studio: Memory cleared.")

    else:
        messages.append({"role": "user", "content": text})
        # Why: keep the system message plus only the last N messages so the
        # tokens sent (and the cost) stop growing in a long chat.
        messages = [messages[0]] + messages[1:][-config["max_messages"]:]

        start = time.perf_counter()
        response = precise.invoke(messages)
        total_seconds += time.perf_counter() - start

        messages.append({"role": "assistant", "content": response.text})
        total_tokens += response.usage_metadata["total_tokens"]
        chat_answers += 1

        print(f"Studio: {response.text}")
        print(
            f"        (memory: {len(messages)} messages, "
            f"{response.usage_metadata['input_tokens']} tokens sent)"
        )

print("=" * 50)
print("Session report")
print(
    f"Chat answers: {chat_answers} | Menu descriptions: {menu_descriptions} | "
    f"Posts: {posts} | Price answers: {price_answers}"
)
print(f"AI usage: {total_tokens:,} tokens in {total_seconds:.1f} seconds")
print("=" * 50)