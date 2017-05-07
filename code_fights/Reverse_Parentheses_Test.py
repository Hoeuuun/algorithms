"""
CF.13

You have a string s that consists of English letters, punctuation marks,
whitespace characters, and brackets. It is guaranteed that the parentheses in
s form a regular bracket sequence.

Your task is to reverse the strings contained in each pair of matching
parentheses, starting from the innermost pair. The results string should not
contain any parentheses.

Example

For string s = "a(bc)de", the output should be
reverseParentheses(s) = "acbde".
"""

s = "a((bcatc))de"

def reverseParentheses(s):
    counter = 0
    pos_first_char = []
    pos_last_char = []
    for i, x in enumerate(s):
        if x == "(":
            #print i, x
            counter += 1
            if s[i+1] != "(":
                print i, x
                pos_first_char = i + 1
    for i, y in enumerate(s):
        if y == ")":
            #print i, y
            counter -= 1
            if s[i-1] != ")":
                print i, y
                pos_last_char = i - 1
    if counter == 0:
        print pos_first_char, pos_last_char, s[pos_first_char:pos_last_char+1]
        char = s[pos_first_char:pos_last_char+1]
        print char[::-1]
    else:
        print "parentheses not balanced"

print reverseParentheses(s)
