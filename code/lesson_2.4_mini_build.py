"""Lesson 2.4: Write a short AI description for every product in one run."""

from langchain.chat_models import init_chat_model

# temp to be set as 0.7 for creativity for marketing text; create model once, outside the loop
writer = init_chat_model("llama3.2", model_provider="ollama", temperature = 0.7)
products = {"chocolate cake": 1500, "cupcake": 250, "brownie": 300, "old stock": 0, "donut": 200}

results = []
total_tokens = 0
total_seconds = 0

for name, price in products.items():
    #items with no price are not for sale
    if price == 0:
        print(f"Skipping {name} (no price)")
        continue

    prompt = f"Write one tempting sentence (max 15 words) for '{name}' at {price} PKR, for a Lahore bakery menu."
    response = writer.invoke([{"role": "user", "content": prompt}])

    results.append({"item": name, "price": price, "text": response.text.strip()})
    total_tokens += response.usage_metadata["total_tokens"]
    total_seconds += response.response_metadata["total_duration"] / 1_000_000_000
print("=" * 50)
for number, row in enumerate(results, start=1):
    print(f"{number}. {row['item'].title()} ({row['price']} PKR)")
    print(f"   {row['text']}")
print("=" * 50)
print(f"{len(results)} descriptions, {total_tokens} tokens, {total_seconds:.1f} seconds")
