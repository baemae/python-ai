""" Generate three useful AI prompts for local businesses and their owners"""
# Asking business details
business_name = input("Business name: ")
Business_type = input("Business Type:   ")
city = input("City:")
cutomers = input("Main customers:")

# taking monthly budget and converting that input str to int
budget = int(input("Monthly budget(PKR):"))

#header with business name
print("\n------------")
print(f"AI Prompt Kit for {business_name}")
print("\n------------")

#Prompt 1 for markteing:
prompt_1 = ( f"Write a short social media post for {business_name},"
            f"a {Business_type} in {city}\n"
            f"Target {cutomers}. Use a professional but friendly tone and include 1 call to action "
            )

print("\n[1]Marketing")
print(prompt_1)

# Prompt for customer service
prompt_2 = (f"You are a manager of {business_name}. Write a polite reply to a customer"
            f"whose order arrived late. Apologise and offer a small discount")
print("\n[2] Customer service")
print(prompt_2)

# Prompt for growth
prompt_3 = (f"Suggest 3 low-cost AI tools a {Business_type} in {city} can use"
            f"to attract {cutomers} within a budgte of {budget} PKR per month")

print("\n[3] Growth")
print(prompt_3)
