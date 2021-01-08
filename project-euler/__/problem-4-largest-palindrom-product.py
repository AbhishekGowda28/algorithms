# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
import helper.palindrom


def problem4():
    first = 999
    second = 999
    highest = 0
    while first > 99 and second > 99:
        product = first*second
        if helper.palindrom.isPalindrom(product) and product > highest:
            highest = product
        second -= 1
        if second < 100:
            first -= 1
            second = 999
    return highest

print(problem4())