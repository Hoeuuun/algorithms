"""
CF.20

Given an array of integers, find the maximal absolute difference between any
two of its adjacent elements.

Example

For inputArray = [2, 4, 1, 0], the output should be
arrayMaximalAdjacentDifference(inputArray) = 3.
"""

inputArray = [1, 1, 1, 1]
def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for i in xrange (0, len(inputArray) - 1):
        diff = abs(inputArray[i+1] - inputArray[i])
        #if diff < 0:
            #diff *= -1
        if diff > max_diff:
            max_diff = diff
    return max_diff

print arrayMaximalAdjacentDifference(inputArray)




"""
inputArray = [-1, 4, 10, 3, -2]
    max_pos = inputArray.index(max(inputArray))
    max_val = max(inputArray)
    left_val = inputArray[max_pos - 1]
    right_val = inputArray[max_pos + 1]
    if max_val - left_val > max_val - right_val:
        return max_val - left_val
    else:
        return max_val - right_val
print arrayMaximalAdjacentDifference(inputArray)
"""
