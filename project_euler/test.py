def is_palindromic(n):
    return n == n[::-1]
    # == (boolean) returns true if n is equal to its reverse

product = 0
for i in xrange(10, 100):
    for j in xrange(10, 100):
        p = i * j
        if is_palindromic(str(p)):
            if p > product:
                product = p
print product
