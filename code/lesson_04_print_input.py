"""Tool for a digital Agency"""

# collects user details and their problems in their business
name = input("Your Name: ")
Type = input("Business Type: ")
prob = input("Biggest Problem: ")

print(f"\nWelcome,{name}!")

# reuseable ai prompt

prompt = f"Suggest 3 AI solutions for a {Type} that struggles with {prob}"

print("---- Your AI Prompt ----")
print(prompt)
