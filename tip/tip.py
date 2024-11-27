#this program calculates tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(tip)


def dollars_to_float(dollars):
    return float(dollars.replace("$", ""))


def percent_to_float(percent):
    return float(percent.replace("%", ""))/100


main()