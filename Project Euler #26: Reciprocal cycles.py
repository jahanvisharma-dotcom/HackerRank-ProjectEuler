def find_cycle(n):
    bool = [0]*n
    bool[1] = 1
    m = 1
    i = 2
    while (True):
        m *= 10
        p = m % n
        if p == 0:
            return 0
        if bool[p]:
            return i-bool[p]
        bool[p] = i
        i += 1
        m = p


ans = [0]*10001
cycle_length = [0]*10001
ans[3] = 3
ans[4] = 3
cycle_length[4] = 1
cycle_length[3] = 1

for i in range(5, 10001):
    p = find_cycle(i)
    if p > cycle_length[ans[i-1]]:
        ans[i] = i
        cycle_length[i] = p
    else:
        ans[i] = ans[i-1]
        cycle_length[i] = cycle_length[i-1]

for _ in range(int(input())):
    n = int(input())
    print(ans[n-1])
