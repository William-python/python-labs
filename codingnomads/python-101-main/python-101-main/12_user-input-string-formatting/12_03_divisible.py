# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
number=input("Pick a number between 1 and 1 billion:")
if int(number) % 3 ==0:
    print(int(number)//3)
else:
    print("Not divisible by 3. Try again.")