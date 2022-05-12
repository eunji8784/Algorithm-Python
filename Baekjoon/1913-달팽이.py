N = int(input())
idx = int(input())
d = [[0] * N for _ in range(N)]

n = 1
mid = (N - 1) // 2
d[mid][mid] = n
x = y = mid

for i in range(3, N + 1, 2):
    x -= 1

    for _ in range(i - 1):
        d[x][y] = n + 1
        y += 1
        n += 1

    y -= 1

    for _ in range(i - 1):
        x += 1
        d[x][y] = n + 1
        n += 1

    for _ in range(i - 1):
        y -= 1
        d[x][y] = n + 1
        n += 1

    for _ in range(i - 1):
        x -= 1
        d[x][y] = n + 1
        n += 1

a = b = 0
for i in range(N):
    for j in range(N):
        print(d[i][j], end=' ')
        if d[i][j] == idx:
            a = i + 1
            b = j + 1
    print()

print(a, b)
