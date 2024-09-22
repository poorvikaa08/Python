import random
import art
import wordlist

def playgame():
    print(art.hangman)
    word = random.choice(wordlist.words)

    placeholder = "_" * len(word)
    print(f"Word to guess: {placeholder}")

    '''The below list contains the correct letters of word'''
    correct_letters = []          
        
    lives = 6   
    game_over = False

    while not game_over:
        display = ""             #reset the display at start of each loop


        print(f"You have {lives} lives remaining")
        user_guess = input("Guess a letter: ").lower()
        
        if user_guess in correct_letters:
            print("\nYou guessed this letter already!")
            continue           #skip the current iteration
        
        if user_guess in word:
            print("\nGood guess!")
            correct_letters.append(user_guess)
        else:
            lives -= 1
            print("\nWrong guess!")  
            
            
            
        for letter in word:
            if letter in correct_letters:
                display += letter
            else:
                display += "_"
                
        print(f"Word to guess: {display}")
        print(art.stages[lives])                #shows the correct hangman stage
        
        
        #check if the player guessed the entire word
        if "_" not in display:
            game_over = True
            print("Congratulations!! You guessed the word")
        
        if lives == 0:
            game_over = True 
            print(f"GAME OVER! You ran out of lives\nThe word was {word}")
               
    choice = input("\nDo you want to play again\nType 'yes' or 'no': ").lower()
    if choice == "yes":
        playgame()
    else: 
        exit
        
playgame()