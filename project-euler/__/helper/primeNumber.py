import math


def primeNumbers(start, last):
    if last < 2:
        print("Prime Numbers cannot be found")
        return []
    rangeList = defineRange(start, last+1)
    primes = []

    for count in range(2, math.ceil(math.sqrt(last))):
        for block in rangeList:
            if block[0] % count == 0 and block[0] != count and block[1] == True:
                block[1] = False
    for block in rangeList:
        if block[1] == True:
            primes.append(block[0])

    return primes


def isPrime(number):
    primes = primeNumbers(2, number)
    return primes.__contains__(number)


def defineRange(start, end):
    rangeList = []
    if start > 1 and end > 1:
        if start < end:
            for number in range(start, end):
                rangeList.append([number, True])
        else:
            for number in range(end, start):
                rangeList.append([number, True])
    return rangeList