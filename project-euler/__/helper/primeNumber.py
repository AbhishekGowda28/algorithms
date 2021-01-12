import math


def primeNumbers(start, last):
    if last < 2:
        print("Prime Numbers cannot be found")
        return []
    rangeList = defineRange(start, last+1)
    primes = [2]
    mark = 0
    count = rangeList[mark][0]
    while count < math.ceil(math.sqrt(last+1)):
        for block in rangeList[mark+1:]:
            if block[0] % count == 0 and block[0] != count and block[1] == True:
                block[1] = False
        mark += 1
        while rangeList[mark][1] == False:
            mark += 1
        count = rangeList[mark][0]

    for block in rangeList:
        if block[1] == True:
            primes.append(block[0])

    return primes


def isPrime(number):
    if number != 2 and number % 2 == 0:
        return False
    primes = primeNumbers(2, number)
    return primes.__contains__(number)


def defineRange(start, end):
    rangeList = []
    if start > 1 and end > 1:
        if start < end:
            for number in range(start, end):
                if number % 2 != 0:
                    rangeList.append([number, True])
        else:
            for number in range(end, start):
                if number % 2 != 0:
                    rangeList.append([number, True])
    return rangeList
