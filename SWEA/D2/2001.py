T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(N)]
    max_val = 0

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            val = 0
            tmp_i = i
            for _ in range(M):
                tmp_j = j
                for _ in range(M):
                    val += array[tmp_i][tmp_j]
                    tmp_j += 1
                tmp_i += 1
            if val > max_val:
                max_val = val

    print("#{} {}".format(test_case, max_val))
