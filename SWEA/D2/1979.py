T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N):
        col_count = 0
        row_count = 0
        for j in range(N):
            if array[i][j] == 1:
                col_count += 1
                if col_count == K:
                    if (j + 1) == N:
                        res += 1
                    elif array[i][j + 1] == 0:
                        res += 1
            else:
                col_count = 0

            if array[j][i] == 1:
                row_count += 1
                if row_count == K:
                    if (j + 1) == N:
                        res += 1
                    elif array[j + 1][i] == 0:
                        res += 1
            else:
                row_count = 0

    print("#{} {}".format(test_case, res))
