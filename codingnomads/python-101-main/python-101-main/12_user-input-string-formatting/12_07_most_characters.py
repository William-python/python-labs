# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings
first = input("Please input the first sentence.")
second = input("Please input the second sentence.")
third = input ("Please input the third sentence.")
lenfirst= len(first)
lensecond= len(second)
lenthird= len(third)
if lenfirst>lensecond and lenfirst>lenthird:
    print(first,lenfirst)
elif lensecond>lenfirst and lensecond>lenthird:
    print(second,lensecond)
else:
    print(third,lenthird)