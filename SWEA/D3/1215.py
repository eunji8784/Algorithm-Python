T = 10
N = 8

for test_case in range(1, T + 1):
    K = int(input())
    array = [list(input()) for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N - K + 1):
            tmp1 = ''
            tmp2 = ''
            for k in range(K):
                tmp1 += array[i][j + k]
                tmp2 += array[j + k][i]
            if tmp1 == "".join(list(reversed(tmp1))):
                count += 1
            if tmp2 == "".join(list(reversed(tmp2))):
                count += 1

    print("#{} {}".format(test_case, count))
