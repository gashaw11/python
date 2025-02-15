amount_due = int(input("amount due "))
while amount_due > 0:
    print(amount_due)
    insert_coin = int(input("enter coin "))
    if insert_coin in [5,15,25]:
        amount_due -= insert_coin
    else:
        print("invalide amount")
change_owed = abs(amount_due)
print(change_owed)