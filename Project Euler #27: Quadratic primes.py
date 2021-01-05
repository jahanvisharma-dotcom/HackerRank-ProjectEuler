from math import sqrt
from itertools import count,islice
def primes(n):
    numbers=set(range(n-1,1,-1))
    prime=[]
    while numbers:
        k=numbers.pop()
        prime.append(k)
        numbers.difference_update(set(range(k*2,n,k)))
    return prime
def check(n):
    return n>1 and all(n%i for i in islice(count(2),int(sqrt(n))-1))
def conset(ab):
    a,b=ab[0],ab[1]
    for i in count():
        n=i*(i+a)+b
        if not check(n):
            return i
n=int(input())
b=primes(n)
a=list(range(-n,n+1,2)) if n&1 else list(range(-n+1,n,2))
s=max(((i,j) for i in a for j in b),key=conset)
print(str(s[0]),str(s[1]))
