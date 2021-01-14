from helper import primeNumber


def problem12():
    sum = 0
    counter = 0
    while True:
        factors = getFactors(sum)
        if len(factors) > 500:
            print(factors)
            return sum
        counter += 1
        sum = (counter*(counter+1))/2   
    return sum


def getFactors(number):
    factors = []
    counter = 1
    while counter <= number:
        if number % counter == 0:
            factors.append(counter)
        counter += 1
    return factors


print(problem12())
