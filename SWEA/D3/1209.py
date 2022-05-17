T = 10
N = 100

for test_case in range(1, T + 1):
    t = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    max_v = array[0][0]

    # 행의 합
    for i in range(N):
        sum_v = sum(array[i])
        if sum_v > max_v:
            max_v = sum_v

    # 열의 합
    for i in range(N):
        sum_v = 0
        for j in range(N):
            sum_v += array[j][i]
        if sum_v > max_v:
            max_v = sum_v

    sum_v = 0
    # 오른쪽 아래 방향 대각선의 합
    for i in range(N):
        sum_v += array[i][j]
    if sum_v > max_v:
        max_v = sum_v

    sum_v = 0
    # 왼쪽 아래 방향 대각선의 합
    for i in range(N):
        sum_v += array[i][N - 1 - i]
    if sum_v > max_v:
        max_v = sum_v

    print("#{} {}".format(t, max_v))
