
#submit50 cs50/problems/2022/python/outdated
#using map to convert the iterables to int
#using split and strip methods

#submit50 cs50/problems/2022/python/outdated

from datetime import datetime

# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Get user input
date = input("Date (e.g., January 5, 2023 or mm/dd/yyyy): ").strip()

try:
    if "/" in date:
        # Handle MM/DD/YYYY format
        month, day, year = map(int, date.split("/"))  # Convert to integers
    else:
        # Handle "Month Day, Year" format
        month_str, day_year = date.split(" ", 1)  # Split at first space
        day, year = map(str.strip, day_year.split(","))  # Remove extra spaces
        day, year = int(day), int(year)  # Convert to integers
        month = months.index(month_str.capitalize()) + 1  # Convert month name to number
    
    # Validate and format the date
    formatted_date = datetime(year, month, day).strftime("%Y-%m-%d")
    print(formatted_date)

except (ValueError, IndexError):
    print("Invalid date format. Please enter a valid date.")
