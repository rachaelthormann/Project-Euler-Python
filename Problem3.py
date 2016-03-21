"""
File name: Problem3.py
Description: This program will find the largest prime factor
            of the number 600851475143.
Author: Rachael Thormann
Date Created: 3/21/2016
Date Last Modified: 3/21/2016
Python Version: 3.4
"""

def largest_prime_factor(num):
    """Finds the largest prime factor."""
    i = 2
    # largest prime factor will never be greater than square root of i
    # because we divide the divisors out of the number
    while i * i <= num:
        
        # if n divides evenly by i, replace num by num // i
        if (num % i == 0):
            num //= i
                    
        # increment i
        else:
            i += 1
    print(num)

largest_prime_factor(600851475143) 
