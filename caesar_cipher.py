#encryption and decryption

logo = '''
╔═╗┌─┐┌─┐┌─┐┌─┐┬─┐  ╔═╗┬┌─┐┬ ┬┌─┐┬─┐
║  ├─┤├┤ └─┐├─┤├┬┘  ║  │├─┘├─┤├┤ ├┬┘
╚═╝┴ ┴└─┘└─┘┴ ┴┴└─  ╚═╝┴┴  ┴ ┴└─┘┴└─
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            
print(logo)


def caesar(choice, message, shift):
    if choice == "decode":
        shift *= -1
    output = ""        

    for letter in message:
        if letter not in alphabet:
            output += letter
        else:   
            shifted_index = alphabet.index(letter) + shift
            shifted_index %= len(alphabet)
            output += alphabet[shifted_index]

    print(f"Your {choice}d message : {output}")
            


should_continue = True
while should_continue:
    choice = input("Do you want to encrypt or decrypt?\nType 'encode' to encrypt or 'decode' to decrypt\n").lower()
    message = input("Type your message: ").lower()
    shift = int(input("Enter the shift number: "))

    caesar(choice, message, shift)
    
    restart = input("Would you like to encode or decode again : \nType 'yes' or 'no'").lower()

    if(restart== "no"):
        should_continue = False
        print("Thank you!!")
        

# For encryptuing and decrypting seperately

'''
def caesar(choice, message, shift):

    if choice == "encode":
        def encrypt(message, shift):
            cipher_text = ""
            for letter in message:
                shifted_index = alphabet.index(letter) + shift
                shifted_index %= len(alphabet)
                cipher_text += alphabet[shifted_index]
                
            print(f"Your encoded message is {cipher_text}")
            
        encrypt(message, shift)
    elif choice == "decode":
        def decrypt(message, shift):
            cipher_text = ""
            for letter in message:
                shifted_index = alphabet.index(letter) - shift
                shifted_index %= len(alphabet)
                cipher_text += alphabet(shifted_index)
                
            print(f"Your decoded message is {cipher_text}")
    else:
        print("Invalid")     
'''
