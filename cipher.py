# add your code here
# Your task for the bonus exercise is the implementation of a Caesar cipher with a variable shift. The program should ask
# the user for a number of characters for the shift first. Next the program should ask the user for a plain text sentence
# and print the encrypted text. Here is an example execution of the program:

#     Please enter the number of places to shift: 5
#     Please enter a sentence: python is fun!
#     The encrypted sentence is: udymts nx kzs!


users_shift = int(input("Please enter the number of places to shift:"))
users_text = input("Please enter a sentence:")
encrypted_text = ""
for ltr in users_text:
    shifted_chr = ord(ltr) + users_shift
    if(ltr == " "):
        encrypted_text = encrypted_text + " "
    else:    
        encrypted_text = encrypted_text + chr(shifted_chr)
print("encrypted text is:", encrypted_text)

