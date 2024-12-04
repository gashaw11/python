#submit50 cs50/problems/2022/python/outdated
#using map to convert the iterables to int
#using split and strip methods

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
date = input("Date: ").strip().split("/")

month,day,year=map(int,date)
print(month,day,year)

