# Write your code here
import random
card_number = ""
pin = ""
import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS card")
cur.execute('''CREATE TABLE card
             (id INTEGER, number TEXT, pin TEXT, balance INTEGER DEFAULT 0)''')
conn.commit()

def luhn(num):
    """Adds a checksum to the bank card number using the Luhn algorithm.
    It takes the card number as a string value and returns the card number
    where the last digit replaced by the checksum."""
    num = num[:-1]  # drop the last digit
    list_num = []
    for c, n in enumerate(num, 1):
        n = int(n)
        if c % 2:  # multiply odd digits by 2
            n *= 2
        list_num.append(n - 9 if n > 9 else n)  # subtract 9 to number over 9
    n = sum(list_num) % 10
    return num + str(10 - n if n else n)



while True:
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")

    user_input = input()
    if user_input == "":
        exit()



    if user_input == "1":
        print("Your card has been created")
        print("Your card number:")
        bank_id = random.randint(100000000, 999999999) * 10
        final_number = luhn(str(4000000000000000 + bank_id))
        print(final_number)

        final_pin = ""
        for _ in range(4):
            number = random.randint(0, 9)
            final_pin = final_pin + str(number)

        pin = final_pin
        print("Your card PIN:")
        print(pin)

        cur.execute("INSERT INTO card (id, number, pin, balance) VALUES(?, ?, ?, ?)", (bank_id, final_number, pin, 0))
        conn.commit()

        #for row in cur.execute('SELECT * FROM card;'):
        #    print(row)

        pass
    if user_input == "2":
        print("Enter your card number:")
        entered_card_number = input()
        print("Enter your PIN:")
        entered_pin = input()

        cur.execute('SELECT number FROM card ')
        card_numbers = cur.fetchall()

        cur.execute('SELECT pin FROM card ')
        pin_codes = cur.fetchall()

        flag_number = 0
        flag_pin = 0

        for x in card_numbers:
            if entered_card_number == x[0]:
                flag_number = 1

        for x in pin_codes:
            if entered_pin == x[0]:
                flag_pin = 1





        if flag_number and flag_pin:
            print("You have successfully logged in!")

            while True:
                print('1. Balance')
                print('2. Add income')
                print('3. Do transfer')
                print('4. Close account')
                print('5. Log out')
                print('0. Exit')


                user_input_1 = input()
                if user_input_1 == "1":

                    cur.execute('SELECT balance FROM card WHERE number=?', (entered_card_number,))
                    a = cur.fetchone()
                    conn.commit()

                    print("Balance: ", a[0])

                if user_input_1 == "2":
                    print("Enter income:")
                    cur.execute('SELECT balance FROM card WHERE number=?', (entered_card_number,))
                    a = cur.fetchone()
                    income = input()
                    new_income = a[0] + int(income)
                    cur.execute('UPDATE card SET balance = ? WHERE number=?', (new_income, entered_card_number,))
                    print("Income was added!")
                    conn.commit()

                if user_input_1 == "3":
                    print("Transfer")
                    print("Enter card number:")
                    card_to_tranfer_money = input()

                    card_to_tranfer_money_unchanged = card_to_tranfer_money

                    number_to = luhn(card_to_tranfer_money)

                    if number_to != card_to_tranfer_money:
                        print("Probably you made a mistake in the card number. Please try again!")
                        flag = 0



                    print("Enter how much money you want to tranfer:")
                    money_amount = input()
                    ## check how much money there is

                    cur.execute('SELECT balance FROM card WHERE number=?', (entered_card_number,))
                    a = cur.fetchone()
                    conn.commit()


                    cur.execute('SELECT number FROM card ')
                    lists = cur.fetchall()
                    flag = 0
                    for x in lists:
                        if card_to_tranfer_money == x[0]:
                            flag = 1


                    if a[0] < int(money_amount) and flag != 0:
                        print("Not enough money!")

                    elif flag == 1:

                        number_of_money = a[0] # balance in bank from which i will transfer

                        money_to_transfer = int(money_amount)

                        number_of_money = a[0] - int(money_amount)

                        cur.execute('UPDATE card SET balance = ? WHERE number=?',
                                    (number_of_money, entered_card_number,))
                        conn.commit()

                        cur.execute('UPDATE card SET balance = ? WHERE number=?',
                                    (money_to_transfer, card_to_tranfer_money_unchanged,))
                        conn.commit()
                        print("Success!")


                    else:

                        print("Such a card does not exist.")





                if user_input_1 == "4":
                    cur.execute('DELETE from card WHERE number=?', (entered_card_number,))
                    conn.commit()
                    print("The account has been closed!")
                    for row in cur.execute('SELECT * FROM card;'):
                        print(row)
                    break




                if user_input_1 == "5":
                    print("You have successfully logged out!")
                    break
                if user_input_1 == "0":
                    exit()
        else:
            print("Wrong card number or PIN!")
        pass





    if user_input == "0":
        print("Bye!")
        exit()
