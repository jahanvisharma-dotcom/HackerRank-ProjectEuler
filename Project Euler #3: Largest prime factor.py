#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i=2
    while i <= n**0.5:
        if n%i==0:
            n = n//i
        else:
            # edge case is i==2 where we add 1
            if i==2:
                i=3
            else:
                i+=2
    print(n)
