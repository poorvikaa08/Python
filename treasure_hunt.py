import art

print('''
▄▄▄▄▄▄▄▄  ▄▄▄ . ▄▄▄· .▄▄ · ▄• ▄▌▄▄▄  ▄▄▄ .     ▄ .▄▄• ▄▌ ▐ ▄ ▄▄▄▄▄    
•██  ▀▄ █·▀▄.▀·▐█ ▀█ ▐█ ▀. █▪██▌▀▄ █·▀▄.▀·    ██▪▐██▪██▌•█▌▐█•██      
 ▐█.▪▐▀▀▄ ▐▀▀▪▄▄█▀▀█ ▄▀▀▀█▄█▌▐█▌▐▀▀▄ ▐▀▀▪▄    ██▀▐██▌▐█▌▐█▐▐▌ ▐█.▪    
 ▐█▌·▐█•█▌▐█▄▄▌▐█ ▪▐▌▐█▄▪▐█▐█▄█▌▐█•█▌▐█▄▄▌    ██▌▐▀▐█▄█▌██▐█▌ ▐█▌·    
 ▀▀  .▀  ▀ ▀▀▀  ▀  ▀  ▀▀▀▀  ▀▀▀ .▀  ▀ ▀▀▀     ▀▀▀ · ▀▀▀ ▀▀ █▪ ▀▀▀     
''')


print("\n\nWelcome to Treasure Hunt.")
print("Your mission is to find the treasure.")

choice1 = input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\"\n").lower()

if choice1 == "right":
    choice2 = input("You've reached the shore of an ocean.\n"
                    "You see an island nearby. "
                    "Do you want to wait for a boat or swim?\n"
                    "Type \"wait\" or \"swim\"\n").lower()
    if choice2 == "wait":
        choice3 = int(input("You arrived at the island unharmed. "
                        "You see a house nearby.\n"
                        "When you enter the house, you see 3 doors. "
                        "Which door among 3 do you choose?\n"
                        "Type 1 or 2 or 3\n"))
        if choice3 == 2:
            print("Hurray!!\nYou found the treasure. You WIN\n\n")
            print(art.treasure)
        elif choice3 == 1:
            print("It's a room full of bats!!\nGAME OVER!!")
        elif choice3 == 3:
            print("It's an empty room. You lost!\nGAME OVER!!")
        else:
            print("Invalid choice!!\nGAME OVER!!")

    else:
        print("GAME OVER!! A shark attacked you!")
else:
    print("GAME OVER!!\nYou fell inside a deep hole")



