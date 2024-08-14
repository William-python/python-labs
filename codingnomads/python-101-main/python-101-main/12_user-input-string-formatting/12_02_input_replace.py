# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
user_input= input("Enter a sentence and a symbol to replace the first letter with that symbol:")
symbol= input("What symbol do you want?:")
print(user_input)
print(symbol)
print(user_input.replace(user_input[0], symbol))