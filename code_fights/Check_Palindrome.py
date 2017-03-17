"""
CF.3

For inputString = "aabaa", the output should be

checkPalindrome(inputString) = true;

For inputString = "abac", the output should be

checkPalindrome(inputString) = false.
"""

def checkPalindrome(inputString):
    return inputString == inputString[::-1]

inputString = raw_input("enter string: ")
palindrome = checkPalindrome(inputString)
print palindrome
