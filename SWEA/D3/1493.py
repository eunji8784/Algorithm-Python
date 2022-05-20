T = int(input())
N = 300

array = [[0] * N for _ in range(N)]

for i in range(1, N):
    array[i][1] = array[i - 1][1] + i

for i in range(1, N):
    k = i
    for j in range(2, N):
        array[i][j] = array[i][j - 1] + k
        k += 1

for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    xp = yp = xq = yq = 0

    for i in range(1, N):
        for j in range(1, N):
            if array[i][j] == p:
                xp = i
                yp = j
            if array[i][j] == q:
                xq = i
                yq = j
            if xp * yp * xq * yq != 0:
                break

    res = array[xp + xq][yp + yq]

    print("#{} {}".format(test_case, res))
