"""
The Cipher Master: Implement a simple Caesar cipher encryption and decryption program. 
Prompt the user to enter a message and a shift value. Apply the shift to each character
 in the message to create an encrypted version, and vice-versa for decryption.
"""

# read in a message and shift value int
message = input("Enter a message to encrypt: ")
shift = int(input("Enter shift size: "))

# break message into characters. 

encrypted_message = []
for letter in message:
    encrypted_message.append(chr(ord(letter) + shift))
encrypted_message = ''.join(encrypted_message) #this causes a conversion from list to string
print("Encrypted message: " + encrypted_message)

# reverse process to decrypt
decrypted_message = []
for letter in encrypted_message:
    decrypted_message.append(chr(ord(letter) - shift))
decrypted_message = ''.join(decrypted_message)
print('{} decrypts to {}'.format(encrypted_message,decrypted_message))  

# NB this only works for reasonable values of shift
# No wrap-around logic included