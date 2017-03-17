def checkPalindrome(inputString):
    for i in xrange(0, len(inputString)/2):
        if inputString[i] != inputString[-(i+1)]:
            return False
    return True

inputString = raw_input("enter string: ")
palindrome = checkPalindrome(inputString)
print palindrome
