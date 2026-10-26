
"""
Module 1 Checkpoint 2: AI Front Desk
Sweet Crumbs Bakery — a beginner-friendly customer support assistant.
FAQ answers and price quotes use Python rules; other questions get an AI prompt.
"""

# Why: Constants make business prices easy to update in one place.
BOT_NAME = "Sweet Crumbs Desk"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.10

CUPCAKE_PRICE = 250
BROWNIE_PRICE = 300
CHOCOLATE_CAKE_PRICE = 1500
BULK_DISCOUNT_RATE = 0.10

print("=" * 45)
print(f"Welcome to {BOT_NAME}!")
print("Sweet Crumbs Bakery Customer Support")
print("Type /quote for a price estimate or bye to exit.")
print("=" * 45)

customer_name = input("Before we start, what is your name? ").strip().title()

if customer_name == "":
    customer_name = "Customer"

message_count = 0
answered_by_rules = 0
unanswered_count = 0
quotes_count = 0
total_quoted_value = 0
total_estimated_ai_cost = 0
complaints_count = 0

while True:
    message = input(f"\n{customer_name}, how can I help? ")
    message = message.strip().lower()

    # Why: Empty messages should not be treated as real questions.
    if message == "":
        print("Please type a message so I can help you.")
        continue

    message_count += 1

    # Why: Complaints come first so unhappy customers get human support.
    if (
        "refund" in message
        or "complaint" in message
        or "late" in message
        or "problem" in message
    ):
        print(
            "I'm sorry about this experience. "
            "A manager will contact you within 1 hour."
        )
        answered_by_rules += 1
        complaints_count += 1
        continue

    if message == "bye" or message == "exit":
        print(f"Goodbye, {customer_name}! Thank you for contacting us.")
        break

    if message == "human" or "agent" in message:
        print("Connecting you to a human support representative...")
        unanswered_count += 1
        break

    # Why: Check complete greeting words to avoid matching "hi" in "which".
    if (
        message == "hi"
        or message == "hello"
        or message == "hey"
        or message.startswith("hi ")
        or message.startswith("hello ")
        or message.startswith("hey ")
    ):
        print("Hello! How can I help you today?")
        answered_by_rules += 1

    elif (
        "hours" in message
        or "timing" in message
        or "open" in message
        or "close" in message
    ):
        print("We are open every day from 9 AM to 10 PM.")
        answered_by_rules += 1

    elif (
        "location" in message
        or "address" in message
        or "where" in message
    ):
        print(
            "Please contact the bakery for its confirmed address."
        )
        answered_by_rules += 1

    elif (
        "delivery" in message
        or "deliver" in message
        or "shipping" in message
    ):
        print(
            f"Delivery costs PKR {DELIVERY_FEE:,}. "
            f"Orders of PKR {FREE_DELIVERY_LIMIT:,} or more "
            "after discount qualify for free delivery."
        )
        answered_by_rules += 1

    elif (
        "menu" in message
        or "price" in message
        or "prices" in message
        or "items" in message
    ):
        print("Our menu includes:")
        print(f"- Cupcake: PKR {CUPCAKE_PRICE:,} each")
        print(f"- Brownie: PKR {BROWNIE_PRICE:,} each")
        print(f"- Chocolate cake: PKR {CHOCOLATE_CAKE_PRICE:,} each")
        print("Type /quote to calculate an order.")
        answered_by_rules += 1

    elif message == "/quote":
        item = input(
            "Which item? (cupcake, brownie, chocolate cake): "
        ).strip().lower()

        quantity_text = input("How many would you like? ").strip()

        # Why: Validate quantity before int() to prevent a crash.
        if not quantity_text.isdigit():
            print("Please enter a whole-number quantity, such as 2.")
            continue

        quantity = int(quantity_text)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        if item == "cupcake":
            item_price = CUPCAKE_PRICE
        elif item == "brownie":
            item_price = BROWNIE_PRICE
        elif item == "chocolate cake":
            item_price = CHOCOLATE_CAKE_PRICE
        else:
            print(
                "Sorry, that item is not on our menu. "
                "Please ask about cupcakes, brownies, or chocolate cake."
            )
            continue

        subtotal = item_price * quantity
        discount = 0

        if quantity >= 10:
            discount = subtotal * BULK_DISCOUNT_RATE

        discounted_subtotal = subtotal - discount

        if discounted_subtotal >= FREE_DELIVERY_LIMIT:
            delivery = 0
        else:
            delivery = DELIVERY_FEE

        order_total = discounted_subtotal + delivery

        print("\n------ YOUR PRICE QUOTE ------")
        print(f"Item: {item.title()}")
        print(f"Quantity: {quantity:,}")
        print(f"Subtotal: PKR {subtotal:,.2f}")
        print(f"Bulk discount: PKR {discount:,.2f}")
        print(f"Delivery: PKR {delivery:,.2f}")
        print(f"Total: PKR {order_total:,.2f}")
        print("------------------------------")

        quotes_count += 1
        total_quoted_value += order_total
        answered_by_rules += 1

    else:
        # Prepare a prompt for a model; this script does not call a model.
        cleaned_question = message.capitalize()[:150]
        estimated_tokens = round(len(cleaned_question) / 4)

        if (
            "phone" in message
            or "cnic" in message
            or "my address" in message
            or "personal information" in message
        ):
            selected_model = "Local model: llama3.2"
            estimated_cost = 0

            print("\nThis question may contain private information.")
            print("Selected model: Local model (llama3.2)")
            print("Estimated AI cost: PKR 0.00")
        else:
            selected_model = "Cheap cloud model"
            estimated_cost = round(
                estimated_tokens / 1000 * CLOUD_PRICE_PER_1K_TOKENS,
                4,
            )

            print("\nI don't have a rule-based answer for that yet.")
            print(f"Selected model: {selected_model}")
            print(f"Estimated tokens: {estimated_tokens}")
            print(f"Estimated AI cost: PKR {estimated_cost:.4f}")

        # Why: The prepared prompt gives a future AI model useful context.
        ai_prompt = f"""
You are {BOT_NAME}, the customer support assistant for Sweet Crumbs Bakery.
Customer name: {customer_name}
Customer question: {cleaned_question}

Answer politely and clearly. Do not invent prices, policies, or addresses.
If you do not know the answer, recommend contacting bakery staff.
"""
        print("\n------ PREPARED AI PROMPT ------")
        print(ai_prompt)
        print("--------------------------------")

        unanswered_count += 1
        total_estimated_ai_cost += estimated_cost

print("\n" + "=" * 45)
print("SESSION REPORT")
print("=" * 45)
print(f"Customer: {customer_name}")
print(f"Messages received: {message_count}")
print(f"Answered by rules: {answered_by_rules}")
print(f"Sent to AI fallback: {unanswered_count}")
print(f"Quotes completed: {quotes_count}")
print(f"Total quoted value: PKR {total_quoted_value:,.2f}")
print(f"Estimated AI cost: PKR {total_estimated_ai_cost:.4f}")
print(f"Complaints received: {complaints_count}")
print("=" * 45)
