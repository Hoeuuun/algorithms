"""
PE.5

2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

newdict = {}
n = 20
for i in range( 2, n + 1, 1):
    factors = []
    num = i
    p = 2

    for p in range(p, num + 1, 1):
        count = 0
        if i % p == 0:
            while i % p == 0:
                count += 1
                factors.append(p)
                i = i / p

                if p not in newdict:
                    newdict[p] = count

                elif newdict[p] < count:
                    newdict[p] = count

total = 1
for key, value in newdict.iteritems():
    key, value = key, value
    total = total * int(key**value) 
print total
