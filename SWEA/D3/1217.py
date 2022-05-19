T = 10

for test_case in range(1, T + 1):
    t = int(input())
    N, M = map(int, input().split())

    def mul(n, m):
        if m == 0:
            return 1
        else:
            return n * mul(n, m - 1)

    print("#{} {}".format(t, mul(N, M)))
