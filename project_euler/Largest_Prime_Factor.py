"""
PE.3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def is_prime(num):
    if num == 2:
        return True
    # 2 is special case, even prime
    for i in xrange(2, num/2):
    # numbers < 2 are not prime numbers
        if num % i == 0:
            return False
    return True

primes = [2]
for i in xrange(3, 13195, 2):
    if is_prime(i):
        primes.append(i)

def prime_factors(num):
    p = 2
    factors = []
    while True:
        am_i_done = True
        for p in primes:
            if num == p:
                factors.append(p)
            elif num % p == 0:
                num = num / p
                factors.append(p)
                am_i_done = False
                break
        if am_i_done:
            break
    return factors

print prime_factors(600851475143)
print max(prime_factors(600851475143))
