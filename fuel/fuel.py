
#submit50 cs50/problems/2022/python/fuel
#error handinling grassfully
while True:

    try:
        fraction = input("Fraction: ").strip()
        x, y = fraction.split('/')

        x = int(x)
        y = int(y)
        result = x/y*100
        if result>=99:
            print("F")
        elif result<=1:
            print("E")
        else:
            print(result)

        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
