# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4
user_input= input("Enter a sentence and a letter to see where that letter is in the sentence:")
letter= input("What letter do you want to locate?:")
print(user_input)
print(letter)
print(user_input.index(letter))