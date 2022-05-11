T = int(input())
dc = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for test_case in range(1, T + 1):
    fm, fd, sm, sd = map(int, input().split())
    res = 0

    if fm == sm:
        res = sd - fd + 1
    else:
        for i in range(fm, sm):
            res += dc[i - 1]
        res = res - fd + sd + 1

    print("#{} {}".format(test_case, res))
