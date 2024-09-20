import random
import art
print("ROCK - PAPER - SCISSORS")

game_images = [art.rock, art.paper, art.scissors]

player_choice = int(input("What do you choose? Rock, paper or scissors?\nType 0 for rock, 1 for paper and 2 for scissors:  "))
print(game_images[player_choice])

choices = [0, 1, 2]
computer_choice = random.choice(choices)

print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if player_choice >=3 or player_choice <0:
    print("Invalid Number :(")
if player_choice == 0 and computer_choice == 2:
    print("Hurray! You WIN.")
elif player_choice == 2 and computer_choice == 0:
    print("You LOSE!")    
elif player_choice < computer_choice:
    print("You LOSE!")   
elif player_choice > computer_choice:
    print("Hurray! You WIN.")   
elif player_choice == computer_choice:
    print("It's a draw")


