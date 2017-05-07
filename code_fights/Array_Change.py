"""
CF.17

You are given an array of integers. On each move you are allowed to
increase exactly one of its element by one. Find the minimal number of moves
required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
arrayChange(inputArray) = 3.
"""

inputArray = [2, 1, 10, 1]
def arrayChange(inputArray):
    req_moves = 0
    for i in xrange(0, len(inputArray)-1):
        if inputArray[i] < inputArray[i+1]:
            continue
        else:
            req_moves += (inputArray[i] - inputArray[i+1]) + 1
            inputArray[i+1] = inputArray[i]+1
    return req_moves

print arrayChange(inputArray)
