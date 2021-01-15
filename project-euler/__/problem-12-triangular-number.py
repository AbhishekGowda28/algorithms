from math import floor
from helper import primeNumber


def problem12():
    sum = 0
    counter = 1
    while True:
        numberOfFactors = getNumberOfFactos(sum)
        print(sum, numberOfFactors)
        if numberOfFactors > 500:
            return sum
        sum = floor((counter*(counter+1))/2)
        counter = counter + 1
    return sum


def getFactors(number):
    factors = []
    counter = 1
    while counter <= number:
        if number % counter == 0:
            factors.append(counter)
        counter += 1
    return factors


def getNumberOfFactos(number):
    primes = primeNumber.getPrimeFactors(number)
    counter = 0
    index = 0
    originalNumber = number
    product = 1
    while index < len(primes):
        divisor = primes[index]
        if number % divisor == 0:
            counter += 1
            number = floor(number/divisor)
        else:
            number = originalNumber
            index += 1
            product *= (counter+1)
            counter = 0
    return product


print(problem12())
