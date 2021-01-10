# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

from helper import primeNumber


def problem5():
    count = 2
    lcm = 1
    while count < 21:
        lcm = math.floor((lcm * count)/math.gcd(lcm, count))
        count += 1
    return lcm


print(problem5())
