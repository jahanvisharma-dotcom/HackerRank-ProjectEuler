#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total = 0
    a = 0
    b = 1
    while b < n:
        if b%2==0:    #even
            total += b
        a,b = b,a+b
    print(total)
