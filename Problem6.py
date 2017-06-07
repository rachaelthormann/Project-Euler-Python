"""
File name: Problem6.py
Description: Find the difference between the sum of the squares of the first one hundred
             natural numbers and the square of the sum.
Author: Rachael Thormann
Date Created: 6/6/2017
Date Last Modified: 6/7/2017
Python Version: 3.4
"""


def sum_of_squares():
    """This function computes the sum of the squares of numbers from 1 to 100."""
    sumSquare = 0
    for i in range(1, 101):
        sumSquare += i**2

    return sumSquare


def square_of_sum():
    """This function computes the square of the sum of numbers from 1 to 100."""
    squareSum = 0
    for i in range(1, 101):
        squareSum += i

    squareSum = squareSum**2

    return squareSum


def difference():
    """This function computes the difference between the sum of squares and square of the
    sum of numbers from 1 to 100."""

    # this can be computed in one line as follows
    # sum([x for x in range(101)]) ** 2 - sum([x ** 2 for x in range(101)])

    # we will make use of the functions above
    return square_of_sum() - sum_of_squares()

print(difference())
