import math


def primeNumebers(start, last):
    rangeList = defineRange(start, last)
    primes = []
    for count in range(2, math.floor(math.sqrt(last))+1):
        for block in rangeList:
            if block[0] % count == 0 and block[0] != count and block[1] == True:
                block[1] = False
    for block in rangeList:
        if block[1] == True:
            primes.append(block[0])
    return primes


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
