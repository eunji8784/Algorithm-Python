from collections import deque

T = 10

for test_case in range(1, T + 1):
    t = int(input())
    que = deque()
    que.extend(list(map(int, input().split())))

    i = 1
    while True:
        if i > 5:
            i = 1
        tmp = que.popleft() - i
        if tmp <= 0:
            que.append(0)
            break
        que.append(tmp)
        i += 1

    print("#{}".format(t), end=' ')
    print(*que, end=' ')
    print()
