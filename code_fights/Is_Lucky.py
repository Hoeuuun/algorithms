"""
CF.11

Ticket numbers usually consist of an even number of digits.
A ticket number is considered lucky if the sum of the first half of
the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.
"""

n = 1230

def numDigits(n):
    count = 0
    while n > 0:
        n = n/10
        count += 1
    return count
print numDigits(n)

def isLucky(n):
    leftsum = 0
    rightsum = 0
    N = numDigits(n)
    for i in xrange(0, N/2):
        rightsum += n % 10
        n /= 10
    for i in xrange(0, N/2):
        leftsum += n % 10
        n /= 10
    return rightsum == leftsum
print isLucky(n)
