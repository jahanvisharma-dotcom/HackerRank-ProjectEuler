n, k = map(int, input().split())
num_list = [str(c) for c in range(1, k+1)]

for i in range(2, n+1):
    string = ''
    for j in range(1, k):
        string += str(i*j)
        items = sorted(list(string))
        if items == num_list:
            print(i)
            break
