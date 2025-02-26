
# import random

# #m = int(input("enter the number of times "))

# while True:
#     probability = input("do you want another number? ")
#     if probability.upper() == "YES":
        
#             n = random.random()
#             #m -= 1

#             print(n)
#     else:
#         break
    



# class Person:
#    def __init__(self, name, age):
#       self.name = name
#       self.age = age

#    def __repr__(self):
#       return f"{self.name},{self.age}"

# p = Person("ali",42)
# print(p)




#print(round(4.64532,2))
#print(tuple([2,3,4]))
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# for enu in enumerate(seasons,1):
#     print(enu)
# from dataclasses import dataclass

# @dataclass
# class InventoryItem:
#     name: str
#     unit_price: float
#     quantity_on_hand: int = 0

#     def total_cost(self) -> float:
#         """Returns the total cost of the inventory item."""
#         return self.unit_price * self.quantity_on_hand

# # Creating multiple inventory items
# inventory = [
#     InventoryItem("Laptop", 1000.0, 5),
#     InventoryItem("Mouse", 25.0, 50),
#     InventoryItem("Keyboard", 45.0, 30),
#     InventoryItem("Monitor", 300.0, 10),
#     InventoryItem("Headphones", 75.0, 20),
# ]

# # Display all inventory items with total cost
# for item in inventory:
#     print(f"{item} → Total Cost: ${item.total_cost():.2f}")

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#     def display(self):
#         return (selfname,self.price)


# item = Item("Laptop", 1000)  # ✅ Works because of __init__
# display = item.display()#consider using list and loop for more obj
# print(display)
# import queue

# orders = queue.Queue()  # Use queue

# # Add orders
# orders.put("Burger")
# orders.put("Pizza")
# orders.put("Pasa")
# orders.put("Buer")
# orders.put("Pza")
# orders.put("Pta")

# # Process orders in FIFO order automatically
# while not orders.empty():
#     order = orders.get()  # Gets the order from the front of the queue
#     print(f"Processing: {order}")
    
#     is_ready = input("Is the order ready? (Yes/No): ").strip()

#     if is_ready.upper() == "YES":
#         print(f"Done: {order}")
#     else:
#         print(f"Order for {order} is not ready yet, retrying...\n")
#         orders.put(order)  # Put the order back in the queue to retry later
#         continue  # Move to the next iteration and retry later

# import os

# folder = "Logs"
# os.makedirs(folder, exist_ok=True)  # Create if not exists

# for i in range(1, 6):  # Create 5 files
#     file_path = os.path.join(folder, f"log_{i}.txt")
#     with open(file_path, "w") as file:
#         file.write(f"This is log file {i}\n")

# print("Files created:", os.listdir(folder))
# import os
# import shutil

# # Define the folder to organize
# downloads_folder = "Downloads"

# # Define categories and their corresponding file extensions
# file_categories = {
#     "Images": [".jpg", ".png", ".gif"],
#     "Documents": [".pdf", ".docx", ".txt"],
#     "Videos": [".mp4", ".mkv"],
# }

# # Ensure category folders exist
# for category in file_categories:
#     os.makedirs(os.path.join(downloads_folder, category), exist_ok=True)

# # Iterate through files and move them into respective folders
# for file in os.listdir(downloads_folder):
#     file_path = os.path.join(downloads_folder, file)
    
#     # Skip directories
#     if os.path.isdir(file_path):
#         continue
    
#     # Move files based on their extension
#     for category, extensions in file_categories.items():
#         if any(file.lower().endswith(ext) for ext in extensions):
#             shutil.move(file_path, os.path.join(downloads_folder, category, file))
#             break


# import os

# # Ensure "Logs" folder exists
# os.makedirs("Logs", exist_ok=True)

# # Now create the file safely
# with open("Logs/old_log.txt", "w") as f:
#     f.write("This is an old log file.")

# print("File created successfully!")


# print("Files organized successfully!")


#turtle
# import argparse

# # Initialize the ArgumentParser
# parser = argparse.ArgumentParser(description="Command-line tool to perform simple tasks")

# # Add arguments
# parser.add_argument('name', type=str, help="Your name")
# parser.add_argument('age', type=int, help="Your age")
# parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose mode")
# parser.add_argument('-c', '--count', type=int, default=5, help="Number of repetitions (default: 5)")

# # Parse the arguments
# args = parser.parse_args()

# # Display the result based on parsed arguments
# if args.verbose:
#     print(f"Verbose mode enabled")

# print(f"Hello {args.name}, you are {args.age} years old.")
# print(f"You will be greeted {args.count} times.")

# # Example of repeating the greeting
# for _ in range(args.count):
#     print(f"Hello, {args.name}!")
# import argparse

# # Initialize the ArgumentParser
# parser = argparse.ArgumentParser(description="A simple program to process a file")

# # Add arguments
# parser.add_argument('filename', type=str, help="The path to the file to be processed")
# parser.add_argument('-l', '--log', action='store_true', help="Enable logging of the process")
# parser.add_argument('--count', type=int, default=10, help="Number of lines to read from the file (default: 10)")

# # Parse the arguments
# args = parser.parse_args()

# # If logging is enabled, print a message
# if args.log:
#     print(f"Logging enabled: Processing file '{args.filename}' with the following settings:")
#     print(f"Lines to read: {args.count}")

# # Try to open and read the file
# try:
#     with open(args.filename, 'r') as file:
#         lines = file.readlines()
#         # Read the specified number of lines
#         for i in range(min(args.count, len(lines))):
#             print(lines[i].strip())  # Remove newline characters from each line
# except FileNotFoundError:
#     print(f"Error: The file '{args.filename}' does not exist.")

# filename = "example.txt"  # Hardcoded filename

# with open(filename, "r") as file:
#     print(file.read())  # Print file content

# import sys

# if len(sys.argv) < 2:
#     print("Usage: python script.py <filename>")
#     sys.exit(1)

# filename = sys.argv[1]  # Get filename from command-line argument

# with open(filename, "r") as file:
#     print(file.read())  # Print file content
# import sys

# if sys.platform == "win32":
#     print("Running on Windows")
# elif sys.platform == "linux":
#     print("Running on Linux")
# elif sys.platform == "darwin":
#     print("Running on macOS")
# import string

# import string
# import random

# def generate_password(length=10):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     return ''.join(random.choices(characters, k=length))

# print(generate_password())  # Example output: 'X2&g@Pz8Wq'
# i="y"
# while i =="y":
#     i = input()
#     print(generate_password())

# import string

# text = "Hello, how are you today? I hope you're doing well!"
# clean_text = ''.join(char for char in text if char not in string.punctuation)
# print(clean_text)  # this is important because ai is efficent when no punctuation. outputs a 
# #clean text and counting words
# import string

# # Create a template string
# template = string.Template("Hello, $name! Welcome to $place.")

# # Substitute values
# result = template.substitute(name="Alice", place="Wonderland")

# print(result)
# import string

# # Create a string format template
# template = "Hello, {name}! Welcome to {place}."

# # Use Formatter to format the string
# formatter = string.Formatter()
# result = formatter.format(template, name="Alice", place="Wonderland")

# print(result)
# Example list of coordinates with city names
# Example list of coordinates with city names
# locations = [
#     ("San Francisco", 37.7749, -122.4194),
#     ("New York", 40.7128, -74.0060),
#     ("Los Angeles", 34.0522, -118.2437)
# ]

# # Format each location and its coordinates using f-strings
# for city, lat, lon in locations:
#     formatted_location = f"City: {city:<115} | Coordinates: Latitude: {lat:.5f}, Longitude: {lon:.5f}"
#     print(formatted_location)

