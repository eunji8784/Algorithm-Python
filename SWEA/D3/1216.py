T = 10
N = 100

for test_case in range(1, T + 1):
    t = int(input())
    array = [list(input()) for _ in range(N)]
    result = 0

    row_array = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(array[j][i])
        row_array.append(tmp)

    for n in range(N, 0, -1):
        if result:
            break
        for i in range(N):
            if result:
                break
            for j in range(N - n + 1):
                tmp1 = array[i][j: j + n]
                tmp2 = row_array[i][j: j + n]
                if tmp1 == tmp1[::-1]:
                    result = len(tmp1)
                    break
                if tmp2 == tmp2[::-1]:
                    result = len(tmp2)
                    break

    print("#{} {}".format(test_case, result))
