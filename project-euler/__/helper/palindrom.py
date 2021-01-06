import math


def numberOfDigits(number):
    digits = 0
    if number < 0:
        number *= -1
    while number > 0:
        number = math.floor(number/10)
        digits += 1
    return digits


def isPalindrom(value):
    originalValue = value
    rev = 0
    counter = numberOfDigits(value)
    while value > 0:
        counter = counter-1
        rem = value % 10
        value = math.floor(value/10)
        rev += math.floor(rem*math.pow(10, counter))
    return originalValue == rev
