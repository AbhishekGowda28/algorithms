# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math


def problem6(limit):
    # f(n) = n/6*(2n+1)*(n+1) ; sum of the squares of the numbers
    sum_sqaure = (limit*((2*limit)+1)*(limit+1))/6
    sum = ((limit*(limit+1))/2) ** 2  # sum(n) = n(n+1)/2
    return math.floor(sum-sum_sqaure)


print(problem6(100))
