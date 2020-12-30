#!/bin/python3
import sys

# Option 1
from functools import reduce
def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = reduce(lambda x,y: x*y/gcd(x,y), range(1,n+1))
    print(int(result))
