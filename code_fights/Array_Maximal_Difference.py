"""
Given an array of integers, find the maximal absolute difference between any
two elements.
"""

inputArray = [2, 100, 1, 1]
def arrayMaximalDifference(inputArray):
    max_current = inputArray[0]
    min_current = inputArray[0]
    for i in xrange(0, len(inputArray)):
        if inputArray[i] > max_current:
            max_current = inputArray[i]
    for i in xrange(0, len(inputArray)):
        if inputArray[i] < min_current:
            min_current = inputArray[i]
    return max_current - min_current

print arrayMaximalDifference(inputArray)

#return max(inputArray) - min(inputArray)
