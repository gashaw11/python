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
date = input("Date (e.g., January 5, 2023: ").strip()

month,day_year = date.split(" ",1)


day,year=day_year.split(",")


# Remove any leading or trailing spaces from day and year
day = day.strip()
year = year.strip()
#month = dates.index(month)
month = month.capitalize()

print(year,month,day)
