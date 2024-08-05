amount_due = 50

while True:

    if amount_due == 0 or amount_due < 0:
        if amount_due < 0:
            amount_due = abs(amount_due)

        print("Change Owed:", amount_due)
        break

    print("Amount Due:", amount_due)
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        amount_due -= insert_coin