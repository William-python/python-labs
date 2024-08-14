# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
word="hello"

# Print an explanation to the user
print("Guess the letters in _ _ _ _ _")

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
man=0
blank="_____"
guess=""

while True:
    print(blank)
    letter=input("Please input a letter:")
    if len(letter)>1:
        print("Only enter one letter")
        continue
    guess+=letter
    if letter in word:
        blank=""
        for ch in word:
            if ch in guess:
                blank+=ch
            else:
                blank+="_"
        if blank==word:
            print("You've got it right.")
            break
    else:
        man+=1
        if man >= 6:
            print("You have lost.")
            break
        print(f"You have {6-man} guesses remaining")    

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it
print('''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""")