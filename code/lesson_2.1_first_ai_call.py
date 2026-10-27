"""Tuition Center tutor.
Asks for a topic and a level (beginner or expert), has an AI model explain the
topic at that level, then prints the answer together with how many tokens the
answer cost and how long it took.
"""
import time
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

#setting a modle and we can change it whenver we need to change it to soem other model or provider
MODEL_NAME = "ollama:gemma4:31b-cloud "

def main()-> None:

    # using .strip() to remove any stary space in the topic string
    topic = input("Topic:  ").strip()
    level = input("Level(beginner or expert):  ").strip()

    #Syestem message that sets the role and the lenth and uses the level

    System_text = (
        "you are a friendly tutor at a tuition center. "
        f"Explain the topic at a {level} level."
        f"Keep the answer to about 3 short sentences"

    )

    #initializing the chat model
    model = init_chat_model(
        MODEL_NAME,
        temperature= 0.2
    )
    # Why: a low temperature (0.2) keeps explanations focused and consistent

    messages = [
        SystemMessage(content=System_text),
        HumanMessage(content=topic)
    ]

    start = time.perf_counter()
    response = model.invoke()
    elapsed = time.perf_counter() - start

   # Why: usage_metadata holds the provider's own token count, so the
    # "cost" we report is exact rather than guessed from word counts.
    total_tokens = response.usage_metadata["total_tokens"]

    print("=" *40)
    print(response.text)
    print("=" * 40)
    print(f"{total_tokens} tokens in {elapsed:.1f} seconds")
 
 
if __name__ == "__main__":
    main()