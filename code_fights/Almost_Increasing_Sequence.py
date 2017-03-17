"""
CF.7

Given a sequence of integers, check whether it is possible to obtain a
strictly increasing sequence by erasing no more than one element from it.

Example

For sequence = [1, 3, 2, 1], the output should be
almostIncreasingSequence(sequence) = false;
For sequence = [1, 3, 2], the output should be
almostIncreasingSequence(sequence) = true.

Constraints:
2 <= sequence.length <= 105,
- 105 <= sequence[i] <= 105.

"""

sequence = [1, 3, 2, 1]
def almostIncreasingSequence(sequence):
    erase = 0
    for i in xrange(0, len(sequence) -1):
        difference = sequence[i+1] - sequence[i]
        if difference > 0:
            continue
        else:
            erase += 1
            if erase > 1:
                return False
    return True
