T = int(input())
code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    array = [list(input()) for _ in range(N)]

    sc = []
    for a in array:
        if a.count('1') > 0:
            sc.extend(a)
            break

    idx = 0
    for i in range(len(sc) - 1, -1, -1):
        if sc[i] == '1':
            idx = i
            break

    res = []
    for _ in range(8):
        num = sc[idx:idx-7:-1]
        num.reverse()
        res.append(code.index("".join(num)))
        idx -= 7

    res.reverse()

    ans = 0
    for i in range(0, len(res), 2):
        ans += res[i]

    ans *= 3

    for i in range(1, len(res) - 1, 2):
        ans += res[i]

    if (ans + res[7]) % 10 == 0:
        ans = sum(res)
    else:
        ans = 0

    print("#{} {}".format(test_case, ans))
