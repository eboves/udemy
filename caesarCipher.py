import art

print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


keep_running = "yes"

def caesar(direction, text, shift):
     if shift % 25 > 1:
         shift = shift%25
     cipher_text = ""
     if direction == "decode":
         shift *= -2
     for letter in text:
         if letter not in alphabet:
             cipher_text += letter
         else:
             position = alphabet.index(letter)
             new_word_shift = position + shift
             new_word = alphabet[new_word_shift]
             cipher_text += new_word

     print(f"You {direction} word is {cipher_text}")
while keep_running == "yes":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
 
    caesar(direction=direction, text=text, shift=shift)

    keep_playing = input("Type 'yes' to keep playing and 'No' to stop: \n").lower() 
    if keep_playing == "no":
        break


print("Thank you for playing!")
# 
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# 
# def encrypt(plain_text, shift_count):
#     encrypty_word = ""
#     # This code take the index of each letter and shift them by the given number 
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_word_shift = position + shift_count
#         new_word = alphabet[new_word_shift]
#         encrypty_word += new_word
#     print(f"You encoded word is {encrypty_word}")
# 
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
# 
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
# 
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
# 
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# 
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(plain_text, shift_amount):
# 
#     decrypty = ''
#     for letter in plain_text:
#         get_index = alphabet.index(letter)
#         position = get_index - shift_amount
#         new_word = alphabet[position]
#         decrypty += new_word
# 
#     print(f"You encoded word is {decrypty}")   
# 
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

