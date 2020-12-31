#!/bin/python3
import sys

limit = 1000000
sum_prime_arr = [0] * limit
prime_arr = [True] * limit
prime_arr[0] = prime_arr[1] = False
for i, isprime in enumerate(prime_arr):
    if isprime:
        sum_prime_arr[i] = sum_prime_arr[i-1] + i
        for n in range(i*i, limit, i):
            prime_arr[n] = False
    else:
        sum_prime_arr[i] = sum_prime_arr[i-1]

t = int(input().strip())
for prime_arr0 in range(t):
    n = int(input().strip())
    print(sum_prime_arr[n])
