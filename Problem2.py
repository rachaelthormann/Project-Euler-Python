"""
Filename: Problem2.py
Description: Consider the terms in the Fibonacci sequence whose
             values do not exceed four million. Find the sum of the
             even-valued terms.
Author: Rachael Thormann
Date Created: 3/20/2016
Date Last Modified: 3/20/2016
Python Version: 3.4
"""

def F(n):
    """Recursive helper function for defining fibonacci numbers."""
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def fibbonacci():
    """Calculates sum as defined in description."""
    i = 0
    summation = 0
    while(F(i) < 4000000):
        if (F(i) % 2 == 0):
            summation += F(i)

        i+=1
        
    print(summation)

fibbonacci()
        
