def palindrome(n):
    newnum=0
    while n>0:
        newnum = newnum*10 + n % 10
        n//=10
    return newnum == n
