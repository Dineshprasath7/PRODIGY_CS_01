print("####################Caesar Cipher############################")
print("\n")

def encrypt(text,shift):
    result=""
    for c in text:
        if (c.isupper()):
           result+=chr((ord(c) + shift -65) % 26 + 65)
           
        else:
            result+=chr((ord(c) + shift -97) % 26 + 97)
    return result

def decrypt(text,shift):
    result=""
    for c in text:
        if(c.isupper()):
            result+=chr((ord(c) - shift - 65) % 26 +65)
        else:
            result+=chr((ord(c) - shift - 97) % 26 +97)
    return result

def main():
        while True:
           action = input("Do you want to encrypt or decrypt a message?\n Input\n'e' for encryption,\n'd' for decryption,\n'q' to quit: ").lower()
           if action == 'q':
               print("\nExiting the program. Goodbye!")
               return
           else:
               print("\nInvalid action. Please choose 'e', 'd', or 'q' to quit.")
    
           if action == 'q':
               return
           
           if action == 'e':
               text=input("Enter text to encrypt:")
               shift=int(input("Enter shift value:"))
               x=encrypt(text, shift)
               print("Encrypted text : ",x)
           elif action == 'd':
               text=input("Enter text to decrypt:")
               shift=int(input("Enter shift value:"))
               x=decrypt(text, shift)
               print("Decrypted text : ",x)
            
            
if __name__=="__main__":
    main()    