
"""A simple clinic chatbot for answering common customer questions.

Designed for a local clinic that receives repeated questions about
opening hours, fees, location, and appointments.
"""

print("City Care Bot: Hi! Ask about timings, fees, location or appointments. Type 'bye' to exit.")

# Asking for the name before the loop means we only ask once per conversation.
name = input("City Care Bot: What is your name? ").strip().title()

message_count = 0
unanswered_count = 0
complaint_count = 0

while True:
    # Normalizing every message handles extra spaces and different capital letters.
    message = input(f"{name}: ").strip().lower()
    message_count += 1

    if message == "bye":
        print(f"City Care Bot: Take care, {name}!")
        break

    # Checking complaints first ensures urgent customer problems aren't missed by ordinary intents.
    elif any(word in message for word in ["complaint", "late", "problem", "wrong", "unhappy"]):
        complaint_count += 1
        print("City Care Bot: Sorry about that. The clinic manager will call you today.")

    elif "agent" in message or "human" in message:
        print("City Care Bot: Connecting you to a human...")
        break

    # Exact or startswith checks stop short greetings like 'hi' matching unrelated words.
    elif message == "hi" or message.startswith("hi ") or message == "hello" or message.startswith("hello ") or message == "hey" or message.startswith("hey "):
        print("City Care Bot: Hello! How can I help you today?")

    elif any(word in message for word in ["timing", "hours", "open", "close"]):
        print("City Care Bot: We are open 10 am to 8 pm, Monday to Saturday.")

    elif any(word in message for word in ["fee", "fees", "price", "cost"]):
        print("City Care Bot: Consultation fee is 2,000 PKR.")

    elif any(word in message for word in ["location", "address", "where"]):
        print("City Care Bot: We are at Main Boulevard, Lahore.")

    elif any(word in message for word in ["appointment", "book", "booking"]):
        print("City Care Bot: Please call the clinic to arrange an appointment.")

    else:
        unanswered_count += 1
        ai_prompt = (
            f"You are the friendly assistant of City Care Clinic. "
            f"Answer in 2 lines: {message}"
        )
        print(
            "City Care Bot: I am not sure yet. In Module 2, an AI will answer: "
            f"{ai_prompt}"
        )

print("=" * 40)
print(f"Chat summary: {message_count} messages, {unanswered_count} unanswered.")
print(f"Complaints received: {complaint_count}")
