# Module 1 Checkpoint 2 — AI Front Desk Design

## 1. Business Overview

**Business:** Sweet Crumbs Bakery

**Problem:** Staff repeatedly answer questions about opening hours, location, delivery, and prices. The front desk handles common questions for free, calculates quotes using Python, and prepares AI prompts for questions it cannot answer.

*Business details and prices below are example values for this project. Confirm them with a real business before presenting the tool as a live service.*

## 2. Intent Design Table

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | `refund`, `complaint`, `late`, `problem` | Sorry about that. A manager will call you within 1 hour. |
| Greeting | `hi`, `hello`, `hey` | Hello! How can I help you today? |
| Opening hours | `hours`, `timing`, `open`, `close` | We are open 9 am to 10 pm, every day. |
| Location | `location`, `address`, `where` | Please contact the bakery for its confirmed address. |
| Delivery | `delivery`, `deliver`, `shipping` | Delivery costs 200 PKR, or is free for orders of 3,000 PKR or more. |
| Menu and prices | `menu`, `price`, `prices`, `items` | We offer cupcakes, brownies, and chocolate cakes. Type `/quote` for an estimate. |
| Human support | `agent`, `human` | Connecting you to a human... |

## 3. Business Rules

| Rule | Value |
|---|---|
| Bot name | Sweet Crumbs Desk |
| Cupcake | 250 PKR each |
| Brownie | 300 PKR each |
| Chocolate cake | 1,500 PKR each |
| Bulk discount | 10% off when quantity is 10 or more |
| Delivery fee | 200 PKR |
| Free delivery | Subtotal after discount is at least 3,000 PKR |
| Private keywords | `phone`, `cnic`, `address` |
| Private model | `llama3.2` (local, Ollama) |
| Private model estimated cost | 0 PKR |
| Cloud model | Small cloud model (cheap) |
| Example cloud price | 0.10 PKR per 1,000 tokens |

## 4. Rule Test Table

Run every test and update the Pass? column honestly.

| You type | Expected result | Pass? |
|---|---|---|
| ` WHAT are your hours ` | Hours reply despite capitals and spaces | Pending |
| `which cake is best?` | AI fallback, not a greeting | Pending |
| `my order is late` | Complaint reply | Pending |
| `/quote`, `cupcake`, quantity `1` | Delivery fee charged | Pending |
| `/quote`, `chocolate cake`, quantity `3` | Free delivery when the post-discount subtotal reaches 3,000 PKR | Pending |
| `/quote`, `brownie`, quantity `10` | 10% bulk discount applied | Pending |
| `/quote`, `pizza`, quantity `2` | Polite “not on our menu” message, no crash | Pending |
| `Can I change my phone number?` | Local model; estimated AI cost 0 | Pending |
| Press Enter without typing | Asks again; does not count as a normal message | Pending |
| `BYE` | Goodbye and session report | Pending |
| `/quote`, type letters instead of quantity | Polite validation message; no crash (bonus) | Pending |
| `human` | Connects to human and ends chat (bonus) | Pending |

## 5. Rule Order and Pricing Logic

1. Clean every incoming message using `.strip().lower()`.
2. Handle complaints first so an unhappy customer reaches a human instead of receiving a generic FAQ reply.
3. Handle human handover and `bye`.
4. Handle empty messages and known FAQ intents.
5. Process `/quote` requests using the item price, quantity, discount, and delivery rules.
6. Route unknown questions to a local model if they contain private keywords; otherwise prepare a prompt for a cheap cloud model.
7. Print a session report after the loop ends.

**Quote calculation:**

- Subtotal = item price × quantity.
- Discount = 10% of subtotal when quantity is at least 10.
- Discounted subtotal = subtotal − discount.
- Delivery = 0 when discounted subtotal is at least 3,000 PKR; otherwise 200 PKR.
- Total = discounted subtotal + delivery.

All prices in this design are illustrative. The cloud price is an example for learning cost calculations, not a live provider quote.
