# The sum of the squares of the first ten natural numbers is, 1^2+2^2+...+10^2=385

# The square of the sum of the first ten natural numbers is, (1+2+...+10)^2=55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def problem6():
    count = 1
    sum_sqaure = 0
    sum = 0
    while count < 101:
        sum_sqaure += math.floor(count**2)
        sum+=count
        count+=1
    sum = math.floor(sum**2)
    return math.floor(sum-sum_sqaure)

print(problem6())