# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
user_input=input("Put in a sentence to mock here:")
toupper=True
for ch in user_input:
    if toupper ==True:
        print(ch.upper(),end="")
        toupper=False
    else:
        print(ch.lower(),end="")
        toupper=True
    