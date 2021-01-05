import math


def numberOfDigits(number):
    digits = 0
    if number < 0:
        number *= -1
    while number > 0:
        number = math.floor(number/10)
        digits += 1
    return digits
