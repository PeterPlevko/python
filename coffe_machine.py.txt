# Write your code here
money = 550
water = 400
milk = 540
beans = 120
cups = 9


def print_state():
    global water
    global beans
    global cups
    global money
    global milk
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
{money} of money""")


def main():
    while True:
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
            if coffee == 'back':
                continue
            else:
                buy(coffee)
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == "remaining":
            print_state()
        elif action == "exit":
            break
        else:
            print("Enter correct action!")


def buy(coffee):
    global water
    global beans
    global cups
    global money
    global milk

    if int(coffee) == 1:
        if water >= 250 and beans >= 16 and cups >= 1:
            water -= 250
            beans -= 16
            cups -= 1
            money += 4
            print("I have enough resources, making you a coffee!")
        else:
            print("Not enough supply")

    elif int(coffee) == 2:
        if water >= 350 and beans >= 20 and cups >= 1 and milk >= 75:
            water -= 350
            beans -= 20
            milk -= 75
            cups -= 1
            money += 7
            print("I have enough resources, making you a coffee!")
        else:
            print("Not enough supply")

    elif int(coffee) == 3:
        if water >= 200 and beans >= 12 and cups >= 1 and milk >= 100:
            water -= 200
            beans -= 12
            milk -= 100
            cups -= 1
            money += 6
            print("I have enough resources, making you a coffee!")
        else:
            print("Not enough supply")


def fill():
    global water
    global beans
    global cups
    global milk
    water_add = int(input("Write how many ml of water do you want to add: "))
    water += water_add
    milk_add = int(input("Write how many ml of milk do you want to add: "))
    milk += milk_add
    beans_add = int(input("Write how many grams of coffee beans do you want to add: "))
    beans += beans_add
    cups_add = int(input("Write how many disposable cups of coffee do you want to add: "))
    cups += cups_add


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


main()
