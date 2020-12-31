#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = -1
    for a in range(3, (n//3)+1):
        b = (n**2 - 2*a*n)//(2*n - 2*a)
        c = n - b - a
        if a**2 + b **2 == c**2:
            if a*b*c > result:
                result = a*b*c
    print(result)
