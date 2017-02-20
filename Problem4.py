"""
File name: Problem4.py
Description: Find the largest palindrome made from the product of two 3-digit numbers.
Author: Rachael Thormann
Date Created: 2/19/2017
Date Last Modified: 2/19/2017
Python Version: 3.4
"""

def LargestPalindromeProduct():

    largestProduct = 0

    for i in range(0, 1000):
        for j in range(0, 1000):

            if(len(str(i)) == 3 and len(str(j)) == 3):

                #multiply the two 3 digit numbers together
                product = i * j

                #convert the integer to a string
                productString = str(product)

                #reverse the string for comparison
                reverseString = productString[::-1]

                #test if equal and update largest product
                if(productString == reverseString):
                    if(int(productString) >= largestProduct):
                        largestProduct = int(productString)

    print(largestProduct)

LargestPalindromeProduct()


