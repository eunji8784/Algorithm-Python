T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    N = int(input())

    d = [[0] * N for _ in range(N)]

    n = 1
    x = y = 0
    d[x][y] = n
    while n != N * N:
        for i in range(4):
            for _ in range(N - 1):
                if d[x + dx[i]][y + dy[i]] != 0:
                    break
                x = x + dx[i]
                y = y + dy[i]
                d[x][y] = n + 1
                n += 1
            if n == N * N:
                break

    print("#{}".format(test_case))
    for i in range(N):
        for j in range(N):
            print(d[i][j], end=' ')
        print()
