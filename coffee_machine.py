import coffee_data

def Resources():
    """ Print Report """
    print(f"Water : {resources['water']}ml\nMilk : {resources['milk']}ml\nCoffee : {resources['coffee']}g\nMoney : ${money}")


def menu():
    """Displays the menu"""
    menu = coffee_data.MENU 

    print(">>  MENU  <<")
    print(f"Expresso : {menu["espresso"]["cost"]}\nLatte : {menu["latte"]["cost"]}\nCappuccino : {menu["cappuccino"]["cost"]}")   

    
def coins(quater, dime, nickle, penny):
    # coin operated
    """
    Penny - 1 cent = $0.01
    Dime - 10 cents = $0.10
    Nickel - 5 cents = $0.05
    Quarter - 25 cents = $0.25
    """
    bill = (quater * (0.25)) + (dime * (0.10)) + (nickle * (0.05)) + (penny * (0.01))
    return f"${round(bill,2)}"
 
 
menu()   
coffee_machine = "off"  
menu = coffee_data.MENU 

# 3 flavours
chosen_flavour = input("What would you like to order? (espresso/latte/cappuccino)  : ").lower()
bill = 0
if chosen_flavour in menu.keys():
    if chosen_flavour == "latte":
        bill += menu[chosen_flavour]["cost"]
        print(f"Your bill : ${bill}")
    elif chosen_flavour == "expresso":
        bill += menu[chosen_flavour]["cost"]
else:
    print("Wrong input!")



#print report -- resouces left
resources = coffee_data.resources
money = 0
print("Resources in the coffee machine :- ")
Resources()

#check if available resouces are sufficient?


#Process coins
print("\nPlease insert coins\nType the number of coins to be inserted.")
quater = int(input("Quaters : "))
dime = int(input("Dimes : "))
nickle = int(input("Nickels : "))
penny = int(input("Pennies : "))

total_user_coins = coins(quater, dime, nickle, penny)

