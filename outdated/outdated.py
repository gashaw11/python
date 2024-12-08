
#submit50 cs50/problems/2022/python/outdated
#using map to convert the iterables to int
#using split and strip methods

#submit50 cs50/problems/2022/python/outdated

dates=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date = input("Date (e.g., January 5, 2023 or mm/dd/yyyy: ").strip()

if "/" in date:
    # Handle "MM/DD/YYYY" format
    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        
        print(f"{year:04} {month:02} {day:02}")
    except ValueError:
        pass
else:
    try:   
        month,day_year = date.split(" ",1)


        day,year=day_year.split(",")


        # Remove any leading or trailing spaces from day and year
        day = day.strip()
        year = year.strip()
        #month = dates.index(month)
        month = month.capitalize()
        month = dates.index(month)+1

        print(f"{year:04} {month:02} {day:02}")
    except ValueError:
        pass
