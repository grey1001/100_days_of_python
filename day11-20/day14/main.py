# Importing necessary data from menu module
from menu import MENU,resources,balance

# Defining the value of each coin
nickel = 0.05
penny = 0.01
dime = 0.10
quarter = 0.25

# Flag to keep the coffee machine running
coffee_on = True

# Function to get user's choice of coffee
def choice():
    user = input("What would you like? (espresso/latte/cappucino): ")
    return(user)

# Function to process the coins inserted by the user
def coin_processor():
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("how many pennies?: "))
    accumulator = []
    nickel_amt = nickels * nickel
    accumulator.append(nickel_amt)
    quarter_amt = quarters * quarter
    accumulator.append(quarter_amt)
    dime_amt = dimes * dime
    accumulator.append(dime_amt)
    penny_amt = pennies * penny
    accumulator.append(penny_amt)
    for amount in accumulator:
        total = sum(accumulator)
    return total

# Function to check and print the current resources and balance
def report_check(): 
    for key, value in resources.items():
        if key == 'water' or key == 'milk':
            print(f"{key.title()}: {value}ml")
        elif key == 'coffee':
            print(f"{key.title()}: {value}g")
    for key, value in balance.items():
        print(f"{key}: ${value}")

# Function to check if there are enough resources to make the coffee
def check_resources(ingredients_required):
    for ingredient, amount in ingredients_required.items():
        if resources[ingredient] < amount:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

# Function to process the order based on the total money inserted and the cost of the coffee
def order_processing(total,coffee,cost):
    if total == cost:
        print(f"Here is your {coffee} ☕, enjoy!")
        return True
    elif total < cost:
        print("Sorry that's not enough, money refunded")
        return False
    elif total > cost:
        change = round(total - cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee} ☕, enjoy!")
        return True

# Function to make the coffee, update the resources and balance
def make_coffee(coffee_type, cost):
    global resources, balance
    ingredients_required = MENU[coffee_type]['ingredients']
    if not check_resources(ingredients_required):
        return
    total = coin_processor()
    order_successful = order_processing(coffee=coffee_type, total=total, cost=cost)
    if order_successful:
        for ingredient,amount in ingredients_required.items():
            if ingredient in resources:
                resources[ingredient] -= amount
        balance['Money'] += cost

# Functions to make each type of coffee
def espresso_coffee():
    make_coffee(coffee_type='espresso',cost=1.5)
def latte_coffee():
    make_coffee(coffee_type='latte',cost=2.5)
def cappucino_coffee():
    make_coffee(coffee_type='cappuccino',cost=3.0)

# Main loop to keep the coffee machine running until 'off' is entered
while coffee_on: 
    user_choice = choice()
    if user_choice == "report":
        report_check()
    elif user_choice == 'espresso':
        espresso_coffee()
    elif user_choice == 'latte':
        latte_coffee()
    elif user_choice == 'cappuccino':
        cappucino_coffee()
    elif user_choice == 'off':
        coffee_on = False 

# Message to indicate the coffee machine is shutting down
print("Machine shutting down...")