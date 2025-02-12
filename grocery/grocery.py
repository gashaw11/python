
#submit50 cs50/problems/2022/python/grocery
#using get,sorted methods for {}[]respectively
import json

def grocery_counter():
    """Reads items from user input and saves the data to a file."""
    try:
        with open("grocery_list.json", "r") as file:
            grocery_list = json.load(file)  # Load existing data
    except (FileNotFoundError, json.JSONDecodeError):
        grocery_list = {}  # Start fresh if no file exists

    while True:
        try:
            item = input("Enter item: ").strip().upper()
            grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            break

    # Save updated data back to the file
    with open("grocery_list.json", "w") as file:
        json.dump(grocery_list, file, indent=4)

    return grocery_list  # Return updated dictionary
grocery_list=grocery_counter()
print(grocery_list)
