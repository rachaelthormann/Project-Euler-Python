"""
File name: Problem5.py
Description: Find the smallest possible number that is evenly divisible by all numbers 1-20.
Author: Rachael Thormann
Date Created: 6/5/2017
Date Last Modified: 6/6/2017
Python Version: 3.4
"""


def gcd(x, y):
    """This function computes the greatest common divisor of two numbers."""

    while y:
        # replace x with y, and replace y with x mod y
        x, y = y, x % y

    return x


def lcm(x, y):
    """This function computes the Least Common Multiple of two numbers."""

    # formula for least common multiple
    lcmult = (x * y) // gcd(x, y)

    return lcmult


def evenly_divisible():
    """The smallest number that can is evenly divisible by the numbers 1-20 can
    be found by computing the Least Common Multiple of the numbers 1-20"""

    # find lcm of first two numbers in range
    lcmult = lcm(1, 2)

    # note that lcm(a, b, c) = lcm(lcm(a,b), c)
    for i in range(3, 20+1):
        lcmult = lcm(lcmult, i)

    return lcmult

print(evenly_divisible())

# This is my old version of the program which was extremely slow.
# I have left it commented out here to remind myself that even though a program might
# give the right answer it does not mean that it is efficient.

# def smallestNum():
#     """ Goes through each number and tests if it is evenly divisible by the range specified."""
#
#     # start at 2520 because it is given to us as evenly divisible by 1-10
#     start = 2520
#
#     # loop through each number skipping the ones where they are not divisible by 1-20
#     while not evenlyDivisible(start):
#         start += 1
#
#     # return the number that is evenly divisible by all numbers 1-20
#     return start
#
#
# def evenlyDivisible(num):
#     """ Helper Function.
#         Determines if a number is evenly divisible by all numbers in a range specified."""
#
#     # loop through all numbers 1-20 as specified
#     for i in range(1, 21):
#
#         # test the divisibility of the number passed in
#         if num % i != 0:
#             # return False if not evenly divisible
#             return False
#
#     # return True if evenly divisible by all numbers
#     return True
#
# # call the function and print the answer
# print(smallestNum)

