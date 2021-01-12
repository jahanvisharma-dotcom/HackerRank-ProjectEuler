def valid(n,k):
    s=''
    while n:
        n,r=divmod(n,k)
        s+=str(r)
    return s[::-1]
        
n,k=map(int,input().split())
t=0
for i in range (1, n+1):
    if str(i)==str(i)[::-1]:
        if valid(i,k)==valid(i,k)[::-1]:
            t+=i
print (t)
