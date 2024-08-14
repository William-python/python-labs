# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
user_number=int(input("Please input a number between one and one billion:"))
computer_number=0
while computer_number< user_number:
    computer_number+=1
print(computer_number)