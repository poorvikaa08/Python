def calculate_love_score(name1,name2):
    num1,num2 = 0,0
    name = name1+name2
     
    for letter in name:
        if letter == 'T' or letter == 'R' or  letter == 'U' or letter == 'E':
            num1 += 1
            
    for letter in name:
        if letter == 'L' or letter == 'O' or letter == 'V' or letter == 'E':
            num2 += 1
               
    
    score = str(num1)+str(num2)       
    print(f"Your Love Score is {score}")

print("LOVE CALCULATOR <3")
name1 = input("Your name: ").upper()
name2 = input("Your partner name: ").upper()

calculate_love_score(name1,name2)