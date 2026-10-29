"""Task 2.2: Personal Tutor with Memory"""
from langchain.chat_models import init_chat_model
 
MAX_MESSAGES = 8
llm = init_chat_model("llama3.2", model_provider="ollama")
 
# Why: the system message lives at messages[0] so we can always find it
# again to keep it after /reset and after trimming.
messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly tutor who explains things clearly and "
            "remembers what the student told you. Answer in 3 lines."
        ),
    }
]
questions = []  # stretch: only the user's questions
 
print("Tutor: Ask me anything. Commands: /reset, /count, bye")
 
while True:
    text = input("You: ").strip()  # strip() needs the brackets to actually run
 
    if text.lower() == "bye":
        print("Tutor: Goodbye!")
        if questions:
            print(f"Tutor: You asked {len(questions)} questions.")
            print(f"       First: {questions[0]}")
            print(f"       Last:  {questions[-1]}")
        break
    elif text.lower() == "/reset":
        # Why: we keep messages[0] so the tutor forgets the chat
        # but not its role and rules.
        messages = [messages[0]]
        print("Tutor: Memory cleared.")
    elif text.lower() == "/count":
        print(f"Tutor: {len(messages)} messages in memory.")
    elif text == "":
        print("Tutor: Ask a question")
    else:
        questions.append(text)
        messages.append({"role": "user", "content": text})
        response = llm.invoke(messages)
        messages.append({"role": "assistant", "content": response.content})
 
        # Why: without trimming, every answer re-sends the whole history,
        # so the token cost would grow with every message.
        messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]
 
        print(f"Tutor: {response.content}")
        # Why: input_tokens shows what this answer cost to *send*,
        # which is the number that grows with memory.
        print(f"       (tokens sent: {response.usage_metadata['input_tokens']})")
 