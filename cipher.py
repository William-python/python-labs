lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the 3 mangoes."
cipher = 275


encrypted = ''
for char in secret:
    if not char.isalpha():
        encrypted = encrypted + char
    else :
        index = lowercase_letters.index(char.lower())
        index = index + cipher
        index = index%26 
        encrypted_char = lowercase_letters[index]
        if char.isupper():
            encrypted_char = encrypted_char.upper()
        encrypted= encrypted + encrypted_char

print(encrypted)

#end cipher
#P olhy aol nvvzlilyyplz hyl kvpun dlss aopz flhy, huk zv hyl aol thunvlz