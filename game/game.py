#submit50 cs50/problems/2022/python/game
import random
n=100
level = random.randint(1,n)
while True:
    try:

        guess = int(input("Guess: "))

        if guess < level:
            print("too small")

        elif guess > level:
            print("too large")

        else:
            print("just right")
            break
    except ValueError:
      print("please enter a number between 1 and n")
