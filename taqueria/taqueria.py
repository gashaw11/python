#submit50 cs50/problems/2022/python/taqueria
#using dict methods for calculating toatl price of items in a restaurant menu

items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0

try:
    while True:
        item = input("Item: ").strip().title()
        if item.lower() == "done":
            break
        price = items.get(item)
        if price is not None:
            total_price += price
except EOFError:
    print("done")

print("Total:$",total_price)
