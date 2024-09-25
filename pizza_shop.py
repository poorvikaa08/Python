import art


def order():
    print("Welcome to Pizza Shop")
    choice = input("Would you like to order {YES or NO}? :  ").upper()
    if choice == "YES":
        print("\n",art.pizzaMenu)
        num = 1
        ordered_pizza = []
        pizza_count = int(input("How many pizza would you like to order? : "))
        print("NOTE : Type without space while ordering\n")
        for _ in range(0, pizza_count):
            user_pizza = input("\nWhich pizza would you like to order?  ").lower()
            size = input("Select the size {S, M or L} :  ").upper()
            ordered_pizza.append((user_pizza,size))
            
        cheese = input("\nWould you like to add extra cheese {yes or no}? :  ").lower()
        user_beverages = input("\nBeverages {COKE, ICED SODA or NONE } :  ").lower()
        user_sides = input("\nSides {GARLIC BREAD, CHEESE BALLS or NONE} :  ").lower()
        
        print("\nYour order has been placed")
    else:
        print("Thank you! GOODBYE")
        
    bill = 0
    varient = ["vegloaded", "pannertikka", "pepperoni","veggiedelight", "margherita", "cheeseandcorn"]
    sides = ["garlicbread", "cheeseballs"]
    beverages = {"coke": 89,
                 "iced soda": 79}
    for pizza, sides in ordered_pizza:
        if pizza in varient[0:3]:
            if size == "S":
                bill += 149
            elif size == "M":
                bill += 249
            else:
                bill += 399
        elif pizza == varient[3:6]:    # elif user_pizza in [varient[i] for i in range(3, 6)]
            if size == "S":
                bill += 179
            elif size == "M":
                bill += 299
            else:
                bill += 499
        else:
            None
    
    if cheese == "yes":
        bill += 39
    
    
    if user_beverages in beverages:
        bill += beverages[user_beverages]
    
    
    if user_sides in sides:
        bill += 129
        
    print(f"\nYour total bill : ₹ {bill}")
        
    choice = input("\nDo you want to order again?\nType yes or no: ").lower()
    if choice == "yes":
        order()


order()

    