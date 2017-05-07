"""
CF.16

Two arrays are called similar if one can be obtained from another by swapping
at most one pair of elements in one of the arrays.

Given two arrays, check whether they are similar.

Example

For A = [1, 2, 3] and B = [1, 2, 3], the output should be
areSimilar(A, B) = true.

The arrays are equal, no need to swap any elements.

For A = [1, 2, 3] and B = [2, 1, 3], the output should be
areSimilar(A, B) = true.

We can obtain B from A by swapping 2 and 1 in B.

For A = [1, 2, 2] and B = [2, 1, 1], the output should be
areSimilar(A, B) = false.

Any swap of any two elements either in A or in B won't make A and B equal.
"""

A = [1, 2, 3]
B = [5, 6, 3]

def areSimilar(A, B):
    diff_A = []
    diff_B = []
    diff = 0
    if A == B:
        return True
    if len(A) != len(B):
        return False
    for i in xrange(0, len(A)):
        if A[i] != B[i]:
            print A[i], B[i]
            diff += 1
            diff_A.append(A[i])
            diff_B.append(B[i])
    return sorted(diff_A) == sorted(diff_B) and len(diff_A) == 2
    """
    if diff > 2:
        print diff, "= numbers different"
        return False
    else:
        print diff_A, diff_B
    """
print areSimilar(A, B)
