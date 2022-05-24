T = int(input())

for test_case in range(1, T + 1):
    N, D = map(int, input().split())
    res = 0

    a, b = divmod(N, ((2 * D) + 1))
    if b:
        res = a + 1
    else:
        res = a

    print("#{} {}".format(test_case, res))
