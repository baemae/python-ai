"""Tool for a digital Agency"""

# collects user details and their problems in their business
name = input("Your Name: ")
Type = input("Business Type: ")
prob = input("Biggest Problem: ")
budget = int(input("Monthly budget (PKR): "))

print(f"\nWelcome,{name}!")

# reuseable ai prompt

prompt = ( f"Suggest 3 AI solutions for a {Type} that struggles with {prob}"
f"Budget: {budget} PKR per month." )
print("---- Your AI Prompt ----")
print(prompt)
