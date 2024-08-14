# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
import random
import sys
number=random.randint(1,10)

tries=6
while True:
    guess=input("Please input a number between 1 and 10: ")
    if guess==number:
        print("Congratulations")
        sys.exit()
    if tries==0:
        print("Out of tries")
        sys.exit()
    else:
        print("Try again") 
        tries -=1
