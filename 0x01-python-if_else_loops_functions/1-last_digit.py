#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number % 10
if number  < 0:
    temp = -(temp)
print(f"Last digit of {number:d} is {temp:d} and is", end=" ")
if temp > 5:
    print("greater than 5")
elif temp == 0:
    print("0")
else:
    print("less than 6 and not 0")
