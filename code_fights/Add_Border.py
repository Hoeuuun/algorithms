"""
CF.15

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

addBorder(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
"""

picture = ["abc",
           "ded"]

def addBorder(picture):
    n = len(picture[0])
    top_bottom = ""
    picture_border = []
    for i in xrange(0, n+2):
        top_bottom += "*"
    picture_border.append(top_bottom)
    for i in picture:
        middle = "*" + i + "*"
        picture_border.append(middle)
    picture_border.append(top_bottom)
    return picture_border

def addBorder2(picture):
    n = len(picture[0])
    top_bottom = ""
    for i in xrange(0, n+2):
        top_bottom += "*"
    return [top_bottom] + map(lambda i: '*' + i +'*', picture) + [top_bottom]

print addBorder(picture)
print addBorder2(picture)
