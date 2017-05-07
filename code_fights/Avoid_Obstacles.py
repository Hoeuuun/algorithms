"""

CF.22

You are given an array of integers representing coordinates of obstacles
situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right.
You are allowed only to make jumps of the same length represented by some
integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
avoidObstacles(inputArray) = 4.
"""

inputArray = [5, 3, 6, 7, 9]

def avoidObstaclesBruteForce(inputArray):
    obstacles = sorted(inputArray)

    for step in xrange(2, max(obstacles) + 1):
        good = True
        for j in xrange(0, max(obstacles) + 1, step):
            if j in obstacles:
                good = False
                break
        if good:
            return step
    return max(obstacles) + 1
print avoidObstaclesBruteForce(inputArray)
