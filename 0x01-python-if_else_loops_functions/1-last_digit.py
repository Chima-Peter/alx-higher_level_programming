#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if number < 0:
	number = number * -1
n = number % 10
if temp < 0:
	print("Last digit of {} is -{} and is less than 6 and not 0".format(temp, n))
elif n > 5 and temp > 0:
	print("Last digit of {} is {} and is greater than 5".format(temp, n))
elif n == 0:
	print("Last digit of {} is {} and is 0".format(temp, n))
elif n > 0 and n < 6:
	print("Last digit of {} is {} and is less than 6 and not 0".format(temp, n))
