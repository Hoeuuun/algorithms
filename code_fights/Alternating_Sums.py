"""
CF.14

Several people are standing in a row and need to be divided into two teams.
The first person goes into team 1, the second goes into team 2, the third
goes into team 1 again, the fourth into team 2, and so on.

You are given an array of positive integers - the weights of the people.
Return an array of two integers, where the first element is the total weight
of team 1, and the second element is the total weight of team 2 after the
division is complete.
"""

a = [50, 60, 60, 45, 70]
#      0,  1,  0,  1,  0
#      0 % 2 = 0, 1 % 2 = 1, 2 % 2 = 0, 3 % 2 = 1, 4 % 2= 0

def alternatingSums(a):
    #print a
    answer = [0, 0]
    for i in xrange(0, len(a)):
        answer[i % 2] += a[i]
        #print i, i % 2, answer
    return answer


print alternatingSums(a)
