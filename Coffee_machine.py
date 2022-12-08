"""
☕ Coffee Machine ☕
"""

#This dictionary contains the detailed ingredients and cost for each coffee
menu = {

    "espresso": {

        "ingredients": {

            "water": 50,

            "milk": 0,

            "coffee": 18,

        },

        "cost": 1.5,

    },

    "latte": {

        "ingredients": {

            "water": 200,

            "milk": 150,

            "coffee": 24,

        },

        "cost": 2.5,

    },

    "cappuccino": {

        "ingredients": {

            "water": 250,

            "milk": 100,

            "coffee": 24,

        },

        "cost": 3.0,

    }

}

#This dictionary contains the detailed resources of the machine 
Resources = {
    "water" : 500,
    "milk" : 500,
    "coffee" : 500,
    "money" : 0
}

# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# 3. Print report.

while Resources["water"] > 0: #The machine stays on when has some water
    selected_coffee = input("What would you like?\nA) Espresso\nB) Latte\nC) Cappuccino)\n").lower()

    if selected_coffee == "off":
        print("The machine has been turned off!")
        exit()
    if selected_coffee == "report":
        print(f"water: {Resources['water']} ml\nMilk: {Resources['milk']} ml\nCoffee: {Resources['coffee']} gr\nMoney: ${Resources['money']}")
        exit()
    elif selected_coffee == "a":
        coffee_type = "espresso"
        print(f"You have selected {coffee_type}")
    elif selected_coffee == "b":
        coffee_type = "latte"
        print(f"You have selected {coffee_type}")
    elif selected_coffee == "c":
        coffee_type = "cappuccino"
        print(f"You have selected {coffee_type}")
    else:
        print("Bad request")
        exit()

    # 4. Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.

    if coffee_type == "espresso": #Evaluation of resources for espresso
        if Resources["water"] >= menu["espresso"]["ingredients"]["water"]:
            enough_water = True
        else:
            enough_water = False
            print("Not enough water!")
            exit()
        if Resources["coffee"] >= menu["espresso"]["ingredients"]["coffee"]:
            enough_coffee = True
        else:
            enough_coffee = False
            print("Not enough coffee!")
            exit()

    if coffee_type == "latte": #Evaluation of resources for latte
        if Resources["water"] >= menu["latte"]["ingredients"]["water"]:
            enough_water = True
        else:
            enough_water = False
            print("Not enough water!")
            exit()
        if Resources["coffee"] >= menu["latte"]["ingredients"]["coffee"]:
            enough_coffee = True
        else:
            enough_coffee = False
            print("Not enough coffee!")
            exit()
        if Resources["milk"] >= menu["latte"]["ingredients"]["milk"]:
            enough_milk = True
        else:
            enough_milk = False
            print("Not enough milk!")
            exit()

    if coffee_type == "cappuccino": #Evaluation of resources for cappuccino
        if Resources["water"] >= menu["cappuccino"]["ingredients"]["water"]:
            enough_water = True
        else:
            enough_water = False
            print("Not enough water!")
            exit()
        if Resources["coffee"] >= menu["cappuccino"]["ingredients"]["coffee"]:
            enough_coffee = True
        else:
            enough_coffee = False
            print("Not enough coffee!")
            exit()
        if Resources["milk"] >= menu["cappuccino"]["ingredients"]["milk"]:
            enough_milk = True
        else:
            enough_milk = False
            print("Not enough milk!")
            exit()


#Print for test
    # if coffee_type == "espresso":
    #     print(f"Enough coffee: {enough_coffee}")
    #     print(f"Enough water: {enough_water}")
    # else:
    #     print(f"Enough coffee: {enough_coffee}")
    #     print(f"Enough water: {enough_water}")
    #     print(f"Enough milk: {enough_milk}")


#Final evaluation for resources availability
    if coffee_type == "espresso":
        if enough_water == True and enough_coffee == True:
            resources_evaluation = True
        else:
            resources_evaluation = False
    else:
        if enough_water and enough_coffee and enough_milk == True:
            resources_evaluation = True
        else:
            resources_evaluation = False


# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

    if resources_evaluation == True: #Prompt the user to insert coins when the machine has the resources needed
        quarters = int(input("How meny qarters? "))
        dimes = int(input("How meny dimes? "))
        nickels = int(input("How meny nickels? "))
        pennies = int(input("How meny pennies? "))
        total_incoming = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01) #Calculate the total $ inserted by the user
    
        #Query the cost in dictionary based on coffee selected
        if coffee_type == "espresso":
            cost = menu["espresso"]["cost"]
        elif coffee_type == "latte":
            cost = menu["latte"]["cost"]
        elif coffee_type == "cappuccino":
            cost = menu["cappuccino"]["cost"]

        #Evaluates if the money inserted by the user is enough for the order 
        if total_incoming >= cost:
            preparation = True
        else:
            print(f"${total_incoming} is not enough money for a {coffee_type}\n The cost  is ${cost}")
            exit()
        
        #Modifying resources of machine based on coffee selection
        if preparation == True:
            Resources["money"] += cost
            Resources["water"] -= menu[coffee_type]["ingredients"]["water"]
            Resources["coffee"] -= menu[coffee_type]["ingredients"]["coffee"]
            Resources["milk"] -= menu[coffee_type]["ingredients"]["milk"]

            #Notify the user the preparation of coffee and give the change $
            print(f"Your {coffee_type} has been prepared \n There is ${round((total_incoming - cost), 2)} in change")

            #Prompt the user to make a new order 
            next_order_evaluation = input("Order other coffee? (Y/N)").lower()
            if next_order_evaluation == "y":
                next = True
            else:
                print("The machine has been turned off")
                exit()




"""
💫 Developed by Samuel Ortiz 💫
"""