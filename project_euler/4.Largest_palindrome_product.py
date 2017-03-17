# A palindromic number reads the same both ways.
# The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of
# two 3-digit numbers.

def is_palindromic(n):
    return n == n[::-1]
    # == (boolean) returns true if n is equal to its reverse

product = 0
for i in xrange(100, 1000):
    for j in xrange(100, 1000):
        p = i * j
        if is_palindromic(str(p)):
            if p > product:
                product = p
print product
