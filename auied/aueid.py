import inflect

# Create an inflect engine instance
p = inflect.engine()

names = []  # List to store all names

while True:
    try:
        name = input("name: ").strip()
        if name:  # Add the name only if it's not empty
            names.append(name)
    except EOFError:
        print("\nExiting.")
        break

# Use inflect to format the names into a proper list
if names:
    formatted_names = p.join(names)  # Join the names with commas and "and"
    print("adu", "adu", formatted_names)
else:
    print("No names entered.")
