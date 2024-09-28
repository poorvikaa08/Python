import random
import game_data
import art
import os


def check_answer(guess, c1, c2):
    """ Check who has more followers and returns the answer """
    
    if c1['follower_count'] > c2['follower_count']:
        return guess == 'A'
    else:
        return guess == 'B'
    

data = game_data.data

print(art.higher_lower)

c1 = random.choice(data)
c2 = random.choice(data)

while c1 == c2:
    c2 = random.choice(data)      

score = 0
# Create a flag for while loop
game_over = False

while not game_over:
    
    print(f"Compare A: {c1['name']}, a {c1['description']} from {c1['country']}")
    print(f"Against B: {c2['name']}, a {c2['description']} from {c2['country']}")
    
    
    #Ask user to make a guess
    guess = input("\nWho has more followers?\nChoose 'A' or 'B' : ").upper()

       

        
    ans = check_answer(guess, c1, c2)
    if ans:
        score += 1
        
        #To clear screen after every guess
        if os.name == 'nt':
            os.system('cls')
        else:
            None
            
        print(art.higher_lower)

        
        print("\nYou're right!")
        print(f"Current Score : {score}\n")
        
        c1 = c2        
        c2 = random.choice(data)
        
         
    else: 
        game_over = True
        print("Sorry, that's wrong. You lost")
        print(f"Final score : {score}")
        

    # If both of the choices are same, generate a different one
    while c1 == c2:
        c2 = random.choice(data)      
            
        
