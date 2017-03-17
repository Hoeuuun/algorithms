"""
CF.4

Given an array of integers, find the pair of adjacent
elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be

adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.
"""

def adjacentElementsProduct(inputArray):
    product = inputArray[0] * inputArray[1]
    for i in xrange(0, len(inputArray)-1):
        p = inputArray[i] * inputArray[i+1]
        if p > product:
            product = p
    return product
