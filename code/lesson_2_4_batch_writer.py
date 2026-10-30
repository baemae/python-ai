"""Task 2.4: Batch Product Writer.
 
Writes a one-sentence menu description for every product on a price list in
a single run. Items with price 0 are skipped (no AI call, no tokens spent).
Results are collected in a list of dictionaries, printed as a numbered menu,
followed by a summary of the total tokens and seconds used.
"""
import time

from langchain.chat_models import init_chat_model

products = {
    "Chocolate Cake": 1500,
    "Cupcake": 250,
    "Brownie": 300,
    "Donut": 200,
    "Old stock": 0,
}

# Why: creating the model once, before the loop, avoids paying the setup
# cost again for every product.
llm = init_chat_model("llama3.2", model_provider="ollama", temperature=0.2)

results =[] #one dictionary per item

# Why: accumulators must start at 0 BEFORE the loop; if they were created
# inside it, every product would reset them and we would lose the totals.
total_tokens = 0
total_seconds = 0.0

for name, price in products.items():
    # Why: a price of 0 means "not for sale", so we skip it before calling
    # the AI. That saves time and tokens (and money on a paid model).
    if price == 0:
        print(f"Skipping {name.lower()} (no price)")
        continue

    messages = [{
        "role": "system",
        "content": ("you write menu descriptions for a bakery in lahore."
                    "reply with exactly one sentence and nothing else."),
    },
    {"role": "user", "content": f"Describe this item: {name}"}]
    start = time.perf_counter()
    response = llm.invoke(messages)
    total_seconds += time.perf_counter() - start
 
    total_tokens += response.usage_metadata["total_tokens"]
    results.append({"item": name, "price": price, "text": response.content.strip()})
 
print("=" * 50)
for number, entry in enumerate(results, start=1):
    print(f"{number}. {entry['item']} ({entry['price']} PKR)")
    print(f"   {entry['text']}")
print("=" * 50)
print(f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")
 