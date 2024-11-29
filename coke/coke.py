#submit50 cs50/problems/2022/python/coke
amount_due = int(input("Amount Due: "))


while amount_due > 0:
    print("Amount Due: ",amount_due)
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in [5, 10, 25]:
        amount_due -= insert_coin
    else:
        print("Invalid coin. Please insert 5, 10, or 25 cents.")

change_owed = abs(amount_due)
print("Change Owed: ",change_owed)
