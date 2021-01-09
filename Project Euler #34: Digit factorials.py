f = [1,1,2,6,24,120,720,5040,40320,362880]
ans = 0
for n in range(19,int(input())+1):
    s = sum(f[int(i)] for i in str(n))
    if s%n==0: ans+=n
print(ans)
