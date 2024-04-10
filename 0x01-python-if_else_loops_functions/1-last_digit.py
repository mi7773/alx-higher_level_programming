#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    n = number % -10
else:
    n = number % 10
print(f'Last digit of {number} is {n} and is ', end='')
if n == 0:
    print('0')
elif n > 5:
    print('greater than 5')
else:
    print('less than 6 and not 0')
