"""Lesson 2.2: Sweet Crumbs bot with memory, using a list of messages."""
from langchain.chat_models import init_chat_model

MAX_MESSAGES = 6

llm = init_chat_model("llama3.2", model_provider="ollama")

messages = [
    {"role": "system", "content": "You are a friendly assitant of sweet Crumbs Bakery in Lahore. Answer in  2 short lines"}
]

print("Sweet Crumbs Bot: Ask me anything. Command: /reset, bye")

while True:
    text = input("You: ").strip()
    if text.lower() == "bye":
        break
    elif text =="":
        print("Bot: Please type a questions")
    elif text.lower() == "/reset":
        messages = [messages[0]]  # forget the chat, keep the rules
        print("Bot: Memory cleared.")
    else:
        messages.append({"role": "user", "content": text})
        response = llm.invoke(messages)
        answer = response.content
        messages.append({"role": "assistant", "content": answer})

        print(f"Bot: {answer}")
        input_tokens = response.usage_metadata.get("input_tokens", 0)
        print(f"     (memory: {len(messages)} messages, {input_tokens} tokens sent)")
