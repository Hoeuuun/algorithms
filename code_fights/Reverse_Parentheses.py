"""
CD.13

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

s = "abc(cba)ab(bac)c"

def isValidParenthesis(s):
    i = 0
    for c in s:
        if c == '(':
            i += 1
        if c == ')':
            if i == 0:
                return False
            i -= 1
    return i == 0

def reverseParentheses(s):
    while True:
        done = True
        stack = []
        for i, x in enumerate(s):
            if x == "(":
                done = False
                #print i, x
                stack.append(i)
                #print stack
            if x == ")":
                done = False
                opening_parenthesis_index = stack.pop()
                orig_str = s[opening_parenthesis_index+1:i]
                reverse_str = orig_str[::-1]

                s = s[0:opening_parenthesis_index] + reverse_str + s[i+1:]
                #print "new s", s
                #print reverse_str
                break
        if done:
            break
    return s

print reverseParentheses(s)
