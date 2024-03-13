#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = number * -1
    n = number % 10
    n = n * -1
    number = number * -1
else:
    n = number % 10
if n == 0:
    print("Last digit of", number, "is", n, "and is 0")
elif n < 6:
    print("Last digit of", number, "is", n, "and is less than 6 and not 0")
elif n > 5:
    print("Last digit of", number, "is", n, "and is greater than 5")
