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
date = input("Date (mm/dd/yyyy): ").strip().split("/")

month,day,year=map(int,date)

print(year,dates[month-1],day)
