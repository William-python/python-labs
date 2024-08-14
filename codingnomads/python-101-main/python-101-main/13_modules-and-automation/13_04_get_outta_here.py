# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import sys

while True:
    quit=input('Enter "Quit" to exit the loop')
    if quit== "Quit":
        sys.exit()
    else:
        print("Put Quit in.")
