"""
CF.8

After becoming famous, CodeBots decided to move to a new building and live
together. The building is represented by a rectangular matrix of rooms, each
cell containing an integer - the price of the room. Some rooms are free
(their cost is 0), but that's probably because they are haunted, so all the
bots are afraid of them. That is why any room that is free or is located
anywhere below a free room in the same column is not considered suitable
for the bots.

Help the bots calculate the total price of all the rooms that are suitable
for them.
"""
matrix = [[0, 1, 1, 2], [0, 5, 0, 0], [2, 0, 3, 3]]

def matrixElementsSum(matrix):
    sum = 0
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            # print matrix[i][j],
            if matrix[i][j] == 0:
                print i,  j
                for k in xrange(i + 1, len(matrix)):
                    matrix[k][j] = 0
                    print k, j
            sum += matrix[i][j]
    return sum

print matrixElementsSum(matrix)
