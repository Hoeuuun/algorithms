"""
CF.10

Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

s1 = "aabcc"
s2 = "adcaa"

def commonCharacterCount(s1, s2):
    s1_letter_dict = {}
    s2_letter_dict = {}
    common_list = []
    count = 0
    if len(s1) <= len(s2):
        shorterstring = s1
        longerstring = s2
    else:
        shorterstring = s2
        longerstring = s1
    for i in shorterstring:
        s1_letter_dict[i] = s1_letter_dict.get(i, 0) + 1
    for i in longerstring:
        s2_letter_dict[i] = s2_letter_dict.get(i, 0) + 1
    for k in s1_letter_dict.keys():
        if k in s2_letter_dict.keys():
            common_list.append(k)
    for i in common_list:
        if s1_letter_dict[i] <=  s2_letter_dict[i]:
            count += s1_letter_dict[i]
        else:
            count += s2_letter_dict[i]
    return count

"""
def commonCharacterCount(s1, s2):
    return sum( min(s1.count(i),s2.count(i)) for i in set(s1))
"""
