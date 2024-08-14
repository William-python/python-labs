print("Welcome to the unfulfilling market!")
print("Tell us what you want, and we won't have it.")

food = input("What do you want? ")
amount = int(input(f"How much of {food}? "))

print(f"You want {amount} {food}? Sorry, we only have {amount - 1}.")
