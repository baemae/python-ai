# Module 2, Checkpoint 1: AI Content Studio, Design

Business: Sweet Crumbs bakery, Lahore (replace with your own business if different).

## Facts

| Key | Value |
|---|---|
| name | Sweet Crumbs |
| city | Lahore |
| hours | 9 am to 10 pm, every day |
| delivery | 200 PKR, free for orders from 3,000 PKR |
| phone | 0300-0000000 |
| prices | chocolate cake 1,500 PKR, cupcake 250 PKR, brownie 300 PKR, mango tart 0 (coming soon) |

## Tones

| Tone | Description sent to the AI |
|---|---|
| fun | playful and full of energy, short sentences |
| premium | elegant and calm, focused on quality |
| urgent | exciting and time-limited, makes people act today |

## Which model for which job

| Job | Model and temperature | Why |
|---|---|---|
| Menu descriptions | creative, 0.8 | Marketing text should be varied |
| Social media posts | creative, 0.8 | Posts should sound fresh each time |
| Chat with customers | precise, 0.2 | Answers must stay close to the facts |
| Price questions | no AI | The dictionary gives an exact answer, instantly and for free |

## Feature tests

Fill in "Pass?" with Yes or No after running each row yourself.

| You type | Expected | Pass? |
|---|---|---|
| /menu | Price-0 item skipped, numbered menu, prices with commas | |
| /post fun | Post streams word by word, fun style | |
| /post premium | Post streams word by word, premium style | |
| /post urgent | Post streams word by word, urgent style | |
| /post pirate | Default tone used, no KeyError | |
| /price CUPCAKE | Correct price (250 PKR) | |
| /price mango tart | "Coming soon" | |
| /price donut | "Not on our menu", no crash | |
| My name is Ali, then What is my name? | Remembers the name | |
| /reset, then What is my name? | Does not know | |
| (press Enter with no text) | Asks again | |
| BYE | Goodbye + session report with all numbers | |