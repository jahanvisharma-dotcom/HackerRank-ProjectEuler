one_digit = {'0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
             '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
two_digit = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen',
             '18': 'Eighteen', '19': 'Nineteen', '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
arzesh = {0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: "Trillion"}


def give_three_digit(s):
    # s = string containing 3 digits
    ans = ''
    if s[0] != '0':
        ans += one_digit[s[0]]+' '+'Hundred'+' '
    if s[1] != '0' and s[1] != '1':
        ans += two_digit[s[1]]+' '
    if s[1] == '1':
        ans += two_digit[s[1:]]+' '
    if s[1] != '1' and s[2] != '0':
        ans += one_digit[s[2]]+' '
    if s[1] != '1' and s[2] == '0':
        ans += one_digit[s[2]]
    return(ans)


def solve(n):
    if n == '0':
        print('Zero')
        return
    num = []
    ans = ''
    i = 0
    num.append(n[:len(n) % 3])
    i += (len(n) % 3)
    while i < len(n):
        num.append(n[i:i+3])
        i += 3
    if num[0] == '':
        del(num[0])
    num[0] = '0'*(3-len(num[0]))+num[0]

    N = len(num)
    for i in range(N):
        if num[i] == '000':
            continue
        ans += give_three_digit(num[i])
        ans += arzesh[N-i-1]+' '
    print(ans[:len(ans)-1])


for _ in range(int(input())):
    solve(input())
