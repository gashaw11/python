#submit50 cs50/problems/2022/python/meal
def main():
    time_input = input("what time is it? ").split(":")
    time = convert(time_input)
    if 7.0<= time <=8.0:
        print("break fast")
    elif 12.0<= time <=13.0:
        print("lunch")
    elif 18.0 <= time <=19.0:
        print("dinner")
    else:
        print("none")



def convert(time):
    return int(time[0])+ int(time[1])/60


if __name__ == "__main__":
    main()
