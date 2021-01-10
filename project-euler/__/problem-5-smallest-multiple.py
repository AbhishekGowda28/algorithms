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
