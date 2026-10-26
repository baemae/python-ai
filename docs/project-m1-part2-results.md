# Module 1 Checkpoint 2 — AI Front Desk Test Results

## 1. Test Environment

- **Business:** Sweet Crumbs Bakery
- **AI model:** `llama3.2:latest`
- **Model runner:** Ollama
- **Test type:** Manual prompt testing
- **Important:** The Python front-desk program prepares prompts but does not yet call Ollama automatically. These two tests were run directly in Ollama.

## 2. AI Test 1 — Cake Recommendation

**Prompt used**

> You are the customer support assistant for Sweet Crumbs Bakery.
>
> A customer asks: "Which cake would you recommend for a birthday party of 10 people?"
>
> Recommend a suitable cake from this menu:
> - Cupcake: PKR 250 each
> - Brownie: PKR 300 each
> - Chocolate cake: PKR 1,500 each
>
> Be friendly and concise. Do not invent products, prices, discounts, or bakery policies. If you need more information, ask one short follow-up question.

**Actual model response**

> Happy birthday to the birthday boy or girl!
>
> For a party of 10 people, I would recommend our Chocolate cake, which is priced at PKR 1,500 each. It's a rich, moist, and decadent dessert that's sure to satisfy any chocolate craving. Would you like me to confirm if this cake is suitable for a birthday party, or do you have any other specific requirements?

**Judgement: Partial Pass**

- Correctly recommends a listed menu item and uses the provided price.
- Friendly tone and a relevant follow-up question.
- It invents descriptive product qualities ("rich, moist, and decadent") that were not provided.
- It should clarify the cake's serving size before claiming it suits 10 people.

**Improvement:** Instruct the model to use only verified product information and ask about serving size when it is unknown.

## 3. AI Test 2 — Late Order Complaint

**Prompt used**

> You are the customer support assistant for Sweet Crumbs Bakery.
>
> A customer asks: "My order has not arrived, and I need it for a birthday party tonight. What should I do?"
>
> Apologize, show empathy, and recommend contacting the bakery manager to check the order. Do not promise a refund, delivery time, or compensation that has not been confirmed. Keep the answer concise.

**Actual model response**

> I'm so sorry to hear that your order hasn't arrived yet, especially with your birthday party tonight. I can imagine how stressful that must be. Can you please contact our bakery manager, [Manager's Name], directly so we can investigate what's happened with your order? They'll be able to look into it and provide a solution to get your order to you as soon as possible. Please let them know you need it for a birthday party tonight and they'll do their best to assist you.

**Judgement: Partial Pass**

- Shows empathy and recommends contacting the bakery manager.
- Does not promise a refund or a specific delivery time.
- Includes an unusable placeholder (`[Manager's Name]`).
- "Get your order to you as soon as possible" implies a result that has not been confirmed.

**Improvement:** Tell the model not to use placeholders or promise an outcome. It should recommend contacting the bakery through the business's confirmed contact details.

## 4. Rule-Based Program Tests

Fill the Pass? column only after running and verifying each test.

| Test | Expected result | Pass? |
|---|---|---|
| ` WHAT are your hours ` | Opening-hours reply | Pass |
| `which cake is best?` | AI fallback, not greeting | Pass |
| `my order is late` | Complaint response | Pass |
| `/quote`, `brownie`, `10` | 10% discount and free delivery | Pass |
| `/quote`, `cupcake`, `1` | PKR 200 delivery fee | Pass |
| `/quote`, `pizza`, `2` | Polite unknown-item response | Pass |
| `/quote`, `cupcake`, `abc` | Quantity validation; no crash | Pass |
| Private question containing `phone` | Local model selected, estimated cost PKR 0 | Pass |
| Empty message | Asks user to enter a message | Pass |
| `BYE` | Goodbye and session report | Pass |

## 5. Conclusion

The rule-based front desk handles common questions, complaints, and price calculations without requiring an AI call. The two manual Ollama tests demonstrate how an AI model can draft customer-support answers, but the results also show why prompts need clear limits: the model may invent product descriptions, use placeholders, or imply unconfirmed outcomes.

**Next improvement:** Connect the fallback to Ollama and keep verified business facts and human handover rules under the application's control.