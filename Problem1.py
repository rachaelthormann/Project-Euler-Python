"""
File name: Problem1.py
Descrition: This program will find the sum of all multiples
            of 3 or 5 below 1000.
Author: Rachael Thormann
Date Created: 3/19/2016
Date Last Modified: 3/19/2016
Python Version: 3.4
"""

def multiplesof3and5():
    summation = 0
    for i in range(0, 1000):
        if (i%3 == 0 or i%5 == 0):
            summation += i
            
    print(summation)

multiplesof3and5()

