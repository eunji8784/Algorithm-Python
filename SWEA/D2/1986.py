T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    res = 0

    for i in range(1, N + 1):
        if i % 2 == 0:
            res -= i
        else:
            res += i

    print("#{} {}".format(test_case, res))
