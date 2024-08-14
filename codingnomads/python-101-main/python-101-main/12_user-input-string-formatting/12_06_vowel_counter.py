# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
user_input=input("Input a sentence:")
a=0
e=0
i=0
o=0
u=0
for ch in user_input:
    if ch == "a":
        a+=1
        # short cut of a=a+1
    elif ch == "e":
        e+=1
    elif ch == "i":
        i+=1
    elif ch == "o":
        o+=1
    elif ch == "u":
        u+=1
print(a)
print(e)
print(i)
print(o)
print(u)