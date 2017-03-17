"""
CF.5

Below we will define what and n-interesting polygon is
and your task is to find its area for a given n.

A 1-interesting polygon is just a square with a side of
length 1. An n-interesting polygon is obtained by taking
the n - 1-interesting polygon and appending 1-interesting
polygons to its rim side by side. You can see the 1-, 2- and
3-interesting polygons in the picture below.

Example

For n = 2, the output should be

shapeArea(n) = 5;

For n = 3, the output should be

shapeArea(n) = 13.
"""
def shapeArea_recursive(n):
    if n == 1:
        return 1
    return 4 + (n-2) * 4 + shapeArea_recursive(n - 1)

for i in xrange(2, 10):
    print i, shapeArea_recursive(i), shapeArea_recursive(i) - shapeArea_recursive(i-1)

def shapeArea(n):
    if n == 1:
        return 1
    if n == 2:
        return 5
    walker = 5
    diff_walker = 8
    i = 2
    while i < n:
        walker = walker + diff_walker
        diff_walker = diff_walker + 4
        i = i + 1
    return walker

for i in xrange(2, 10):
    print i, shapeArea(i), shapeArea(i) - shapeArea(i-1)
