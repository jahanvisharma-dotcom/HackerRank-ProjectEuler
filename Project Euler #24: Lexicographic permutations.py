string = "abcdefghijklm"

def find_fac(no):
    i = 1
    while no!=0:
        fac[13 - i] = no % i
        no = no // i
        i += 1
        
    return fac

def find_string(fac):
    arr = list(string)
    result = ""
    
    for i in range(len(fac)):
        result += arr.pop(fac[i])
    
    return result
    
t = int(input())

for i in range(t):
    fac = [0] * 13
    no = int(input())
    no = no - 1
    fac = find_fac(no)
    # print(fac)
    result = find_string(fac)
    print(result)
