from math import log, ceil
def numberOfDigits(n):
    if n==1:
        return 1
    ans = (n * log(1.6180339887498948, 10)) - ((log(5, 10)) / 2)
    return ceil(ans)

testcases = input()
while testcases:
    low, high = 0, 25000
    n = input()
    while low < high:
        mid = (low+high)/2
        mid_n = numberOfDigits(mid)
        if mid_n >= n:
            high = mid
        else:
            low = mid+1
    print((low+high)/2)
    testcases -= 1
