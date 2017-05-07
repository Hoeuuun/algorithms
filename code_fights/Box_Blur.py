"""

CF.23

Last night you had to study, but decided to party instead. Now there is a
black and white photo of you that is about to go viral. You cannot let this ruin
your reputation, so you want to apply box blur algorithm to the photo to hide
its content.

The algorithm works as follows: each pixel x in the resulting image has a value
equal to the average value of the input image pixels' values from the 3 by 3
square with the center at x. All pixels at the edges are cropped.

As pixel's value is an integer, all fractions should be rounded down.

Example

For

image = [[1, 1, 1],
         [1, 7, 1],
         [1, 1, 1]]
the output should be boxBlur(image) = [[1]].

In the given example all boundary pixels were cropped, and the value of the
pixel in the middle was obtained as (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) / 9
= 15 / 9 = ~rounded down~ = 1.


6  2
10 7
"""

image = [
        [0, 18,9],
        [27,9, 0],
        [81,63,45]]

#      0    18  9   27  9 0   81 63 45
#dx = [-1,  0,   1, -1, 0, 1, -1, 0, 1]
#dy = [-1, -1, -1,   0, 0, 0,  1, 1, 1]

def boxBlur(image):
    b = [[]]
    cols = len(image[0])
    rows = len(image)
    for i in xrange(1, rows-1):
        #print i, image[i]
        for j in xrange(1, cols-1):
            #print j, image[i][j]
            sum = 0
            for ii in xrange(i-1, i+2):
                for jj in xrange(j-1, j+2):
                    print ii, jj, image[ii][jj]
                    sum += image[ii][jj]
                    #print sum, image[ii][jj]

            b[i-1].append(sum/9)
        if i != len(image)-2:
            b.append([])
    return b

print boxBlur(image)
