#Try to make an exploding dice roller and a way to add 'encroachment' bonuses to the dice rolls.
#Dice Things:
#Step 1: Get the initial amount of dice rolled from input command.
#Step 2: Figure out how to roll those dice and only keep the highest number rolled.
#Step 3: Check if that highest number is in the explosion range.
#Step 4: If number rolled is in the explosion range, roll another dice.
#Step 5: If the additional dice lands in the explosion range again, roll another dice.
#Step 6: Repeat step 5 until the dice stops landing in the explosion range.
#Step 7: Add the results from all dice rolls into one value and print that value.
#Encroachment Things:
#Step 1: Set up a value to store the current encroachment amount of the character.
#Step 2: Have an input prompt to put in how much encroachment will be gain after rolling.
#Step 3: Modify the character by the amount of encroachment currently in the value (Check DX Book for reference)
#Step 4: Allow a prompt to modify encroachment value without rolling (Used for after session and revival ability.)
#Step 5: Display bonuses from encroachment values and show current encroachment value.
#Step 6: Display Warning for when someone is above 100 Encroachment.
import random
rolls=int(input("Please enter how many dice you wish to roll:"))
total= 0
while rolls > 0:
    number1= random.randint(1,10)
    number2= random.randint(1,10)
    number3= random.randint(1,10)
    number= max(number1,number2,number3)
    print(f"Roll={number}")
    total+= number
    if number >= 10:
        print("Crit")
    else:
        rolls-= 1
print(total)
#