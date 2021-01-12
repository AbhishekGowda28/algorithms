from helper import primeNumber

def problem10():
    primes = primeNumber.primeNumbers(2,10)
    primeSum = 0
    for prime in primes:
        primeSum+=prime
    return primeSum

print(problem10())