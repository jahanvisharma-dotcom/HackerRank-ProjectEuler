#!/bin/python3
import sys

prime_occurences = [0,2,3]

def isPrime(num):
    i = 2
    while i <= int(num**0.5)+1:
        if num % i == 0 and num != i:
            return False
        i += 1
    return True

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    try:
        if prime_occurences[n]:
            print(prime_occurences[n])
    except:
        ptr = len(prime_occurences)
        i = ptr - 1
        num = prime_occurences[i]+1
        while ptr <= n:
            if isPrime(num):
                prime_occurences.append(num)
                ptr += 1
            num += 1
        print(prime_occurences[n])
        
