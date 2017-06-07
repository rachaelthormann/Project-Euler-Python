"""
File name: Problem7.py
Description: Find the 10 001st prime number.
Author: Rachael Thormann
Date Created: 6/7/2017
Date Last Modified: 6/7/2017
Python Version: 3.4
"""


def is_prime(x):
    """This function returns true if the input is a prime number
    and false if it is not."""

    return divmod(2 ** (x - 1), x)[1] == 1

print(is_prime(13))


def find_prime():
    pass


