# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from helper import primeNumber


def problem7():
    primes = primeNumber.primeNumbers(2, 104750)
    return primes[10000]


print(problem7())
