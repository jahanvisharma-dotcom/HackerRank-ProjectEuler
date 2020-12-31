#!/bin/python3
import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()   #this is a string
    result = []
    for i in range(n-k):
        multiply = 1
        for j in num[i:i+k]:
            multiply *= int(j)
        result.append(multiply)
    print(max(result))
