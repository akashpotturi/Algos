import math
def sieve(n):
    isprime = [True]*(n+1)
    isprime[0] = isprime[1] = False
    for i in range(2,math.isqrt(n)+1):
        if isprime[i]:
            for j in range(i*i,n+1,i):
                isprime[j] = False
    return isprime

def getprimeinrange(l,r):
    prime = sieve(math.isqrt(r))
    isprime = [True]*(r-l+1)
    for i in  range(2,math.isqrt(r)+1):
        if not prime[i]:
            continue
        for j in range(max(i*i,(l+i-1)//(i*i)),r+1,i):
            isprime[j-l] = False
    if l == 1:
        isprime[l] = False
    return isprime
