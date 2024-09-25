import random

def secret_text(choice, message):
    
    result = ""
    if choice == "encode":
        if len(message) <= 3:
            for index in range((len(message)-1), -1):
                result += message[index]  
            return result
            
    
choice = input("Do you want to encode or decode: ").lower()
message = input("Type your secret text: ")
print(secret_text(choice, message))
