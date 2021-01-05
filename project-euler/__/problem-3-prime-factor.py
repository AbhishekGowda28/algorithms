# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import math

from helper import primeNumber


def primeFactor(value):
    primes = primeNumber.primeNumebers(
        2, math.floor(math.sqrt(value / 2)))
    factors = []
    for prime in primes:
        if value % prime == 0:
            factors.append(prime)
    print(factors.pop())


primeFactor(600851475143)
