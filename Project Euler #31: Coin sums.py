table = [0] * 100001
coin = [1, 2, 5, 10, 20, 50, 100, 200]
table[0] = 1
for i in range(8):
    for j in range(coin[i], len(table)):
        table[j] += table[j-coin[i]]

for x in range(int(input())):
    num = int(input())
    print(table[num] % 1000000007)
