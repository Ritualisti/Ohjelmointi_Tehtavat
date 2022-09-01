import random

x = random.randint(1,10)
feed = 0
while feed != x:
    feed = int(input("Guess which number "))
    if feed < x:
        print("Your guess is too low")
    elif feed > x:
        print("Your guess is too high")
    else:
        print("You guessed right!")

























