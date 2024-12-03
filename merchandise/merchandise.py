# Merchandise inventory
#a simple merchandise data using dictionaries
# Update quantities
# Apply updates
# Check if updates reflect in the dictionary

merchandise_inventory = {
    "T-Shirt": {"category": "Clothing", "quantity": 50, "price_per_unit": 15.0, "sku": "TS001"},
    "Laptop": {"category": "Electronics", "quantity": 10, "price_per_unit": 1200.0, "sku": "LT001"},
    "Coffee Mug": {"category": "Kitchenware", "quantity": 100, "price_per_unit": 8.0, "sku": "CM001"},
}


bulk_updates = {
    "Coffee Mug": -20,
    "T-Shirt": 15,
    "Laptop": -5
}


for item, quantity_change in bulk_updates.items():
    if item in merchandise_inventory:
        current_quantity = merchandise_inventory[item]["quantity"]
        updated_quantity = current_quantity + quantity_change

        if updated_quantity < 0:
            print(f"Error: Cannot reduce {item} stock below 0.")
        else:
            merchandise_inventory[item]["quantity"] = updated_quantity
            print(f"Updated {item} stock to {updated_quantity}.")
    else:
        print(f"Item '{item}' not found in inventory.")

# Check if updates reflect in the dictionary
print("\nUpdated Merchandise Inventory:")
for item, details in merchandise_inventory.items():
    print(f"{item}: {details}")
