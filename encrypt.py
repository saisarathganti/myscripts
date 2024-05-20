# Simple encrypt code to encrypt and decrypt message

import string

charecters = string.ascii_letters
key = 3 # Set your own key
# print(charecters)

input_message = input("Enter the message to be encrypted:\n")

def encrypt(message):
    new_message = ""
    for charecter in message:
        position = charecters.find(charecter)
        # print(position)
        new_position = (position + key)%26
        new_charecter = charecters[new_position]
        new_message += new_charecter
    return new_message

def decrypt(encrypted_message):
    message = ""
    for char in encrypted_message:
        position = charecters.find(char)
        new_position = (position - key)%26
        message += charecters[new_position]
    return message 

en_msg = encrypt(input_message)
print(en_msg)
print(decrypt(en_msg))