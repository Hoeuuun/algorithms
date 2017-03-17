"""
CF.9

Given an array of strings, return another array containing all of its
longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

inputArray = ["abc","eeee","abcd","dcd"]

def allLongestStrings(inputArray):
    longest = []
    p = 0
    for i in xrange(0, len(inputArray)):
        if len(inputArray[i]) > p:
            p = len(inputArray[i])
    for i in inputArray:
        if len(i) == p:
            longest.append(i)
    return longest

print allLongestStrings(inputArray)
