import art
import random

    
def compare(user_guess, number, attempts):
    if attempts == 0:
       return print("GAME OVER!!")
    if user_guess == number:
        return print(f"\nHurray!! You guessed it right.\nThe number was {number}")        
    elif user_guess < number:
        return print("Too Low!!\nGuess again")  
    else:
        return print("Too High!!\nGuess again")
    
    
def playgame():
    print(art.guess)
    print("Welcome to number guessing game!")
    
    print("Guess a number between 1 to 100")
    level = input("Choose the difficulty level (Hard or Easy) : ").lower()
    
    number = random.choice(range(1,101))
    
    
    if level == "hard":
        attempts = 5
    elif level == "easy":
        attempts = 8
    else:
        print("Invalid")
    
    game_over = False        

    while not game_over:
        
        if attempts == 0:
            game_over == True
            print(f"YOU LOSE!. The number was {number}")
            
            
        if attempts > 0:
            print(f"\nYou have {attempts} attempts remaining to guess the number")
            user_guess = int(input("Make a guess : "))

            compare(user_guess, number, attempts)
            if user_guess != number:
                attempts += -1   
        else:
            game_over = True
            
while input("Do you want to play?\nType 'yes' or 'no' : ").lower() == "yes":
    playgame()
        
        
        
        
        
        