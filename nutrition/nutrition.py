#submit50 cs50/problems/2022/python/nutrition
#using dictionaries to organise data
items = {
    "apple": 52,
    "apricot": 48,
    "avocado": 160,
    "banana": 89,
    "blackberry": 43,
    "blueberry": 57,
    "boysenberry": 50,
    "cantaloupe": 34,
    "cherry": 50,
    "coconut (fresh)": 354,
    "cranberry": 46,
    "date (dried)": 277,
    "dragon fruit": 50,
    "fig (fresh)": 74,
    "grape": 69,
    "grapefruit": 42,
    "guava": 68,
    "honeydew melon": 36,
    "kiwi": 61,
    "lemon": 29,
    "lime": 30,
    "lychee": 66,
    "mango": 60,
    "nectarine": 44,
    "orange": 47,
    "papaya": 43,
    "peach": 39,
    "pear": 57,
    "persimmon": 70,
    "pineapple": 50,
    "plum": 46,
    "pomegranate": 83,
    "raspberry": 52,
    "strawberry": 33,
    "tangerine": 53,
    "watermelon": 30
}
item = input("Item: ")
if item in items:
    print("Calories: ",items[item])
