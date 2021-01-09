import re
set1=set()
sum=0
n=int(input())
for i in range(1964,1,-1):
    for j in range(100):
        if j not in set1:
            value=i*j
            str1=str(value)+str(i)+str(j)
            if value not in set1 :
                matcher=''.join(str(k) for k in range(1,n+1))             
                if(re.fullmatch(matcher,''.join(sorted(str1)))):
                    sum=sum+value                   
                    set1.add(value)
                    
print(sum)
