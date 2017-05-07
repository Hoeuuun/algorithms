"""
CF.18

Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
palindromeRearranging(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""

inputString = "aabc"

def palindromeRearranging(inputString):
    char_list = []
    dict = {}
    for i in inputString:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    for key, value in dict.items():
        if value % 2:
            #print key, value
            char_list.append(key)
    return len(char_list) <= 1

print palindromeRearranging(inputString)
