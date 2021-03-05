# encrypted_message = ""
def encrypt():
  message = input("Enter the message you want to encrypt")
#   ascii_message = [ord(char)+3 for char in message ,if char == " " continue]
  encrypted_message = ""
  for char in message:
    #   encrypted_message = ""
      if char == " ":
          continue
      a = ord(char)+3
      b = chr(a)
      encrypted_message = encrypted_message + b
  return encrypted_message


def decrypt():
    decrypted_message = ""
    message = input("Enter the message you want to decrypt")
    for char in message:
        if char == " ":
            continue
        a = ord(char)-3
        b = chr(a)
        decrypted_message = decrypted_message + b
    return decrypted_message
while True:
    choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
    if choice == 'e':
        print(encrypt())
    elif choice == 'd':
        decrypt()    
    else:
        play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
        if play_again == 'Y':
            continue
        elif play_again == 'N':
            break 
