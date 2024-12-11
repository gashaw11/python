
#submit50 cs50/problems/2022/python/professor
import random

def get_level():
    # Function to get the level of difficulty from the user
    while True:
        try:
            level = int(input("Enter a level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def generate_integer(level):
    # Function to generate two random integers based on the selected difficulty level
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)

def main():
    level = get_level()  # Get the level once
    while True:  # Loop indefinitely until the user decides to quit
        num1, num2 = generate_integer(level)  # Generate a question

        try:
            answer = int(input(f"What is {num1} + {num2}? "))
            if answer != num1 + num2:
                print("Incorrect.")
            # The game continues to the next question regardless of whether the answer is correct or incorrect

        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input

if __name__ == "__main__":
    main()
