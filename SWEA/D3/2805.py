T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input())) for _ in range(N)]
    res = 0

    j = 1
    for i in range(N):
        idx = (N - j) // 2
        res += sum(array[i][idx:idx + j])
        if i < (N - 1) // 2:
            j += 2
        else:
            j -= 2

    print("#{} {}".format(test_case, res))
