import json

def update_inventory(data):
    user_inputs = {}
    while True:
        try:
            item = input("Enter item name to update (or type 'done' to finish): ")
            if item.lower() == 'done':
                break
            if item not in data:
                print("Item not found. Please try again.")
                continue

            print(f"Updating details for '{item}'")
            print("Current data:", data[item])

            key_to_update = input("Enter the attribute to update (category, quantity, price_per_unit, sku): ").lower()
            if key_to_update not in data[item]:
                print("Invalid attribute. Please try again.")
                continue

            new_value = input(f"Enter new value for '{key_to_update}' (current value: {data[item][key_to_update]}): ")
            # Ensure correct data type conversion for quantity and price
            if key_to_update == "quantity":
                new_value = int(new_value)
            elif key_to_update == "price_per_unit":
                new_value = float(new_value)

            data[item][key_to_update] = new_value
            user_inputs[item] = {key_to_update: new_value}
        except Exception as e:
            print(f"Error: {e}")
    return data, user_inputs

# Initial inventory
merchandise_inventory = {
    "T-Shirt": {"category": "Clothing", "quantity": 50, "price_per_unit": 15.0, "sku": "TS001"},
    "Laptop": {"category": "Electronics", "quantity": 10, "price_per_unit": 1200.0, "sku": "LT001"},
    "Coffee Mug": {"category": "Kitchenware", "quantity": 100, "price_per_unit": 8.0, "sku": "CM001"},
}

# Update inventory
updated_inventory, user_changes = update_inventory(merchandise_inventory)

# Save the updated inventory to a file (optional)
with open('updated_inventory.json', 'w') as f:
    json.dump(updated_inventory, f, indent=4)

# Show the updated inventory and user changes
print("Updated Inventory:", updated_inventory)
print("User Changes:", user_changes)
