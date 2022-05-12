T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = [input().split() for _ in range(N)]

    lst_90 = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(a[j][i])
        tmp.reverse()
        lst_90.append(tmp)

    lst_180 = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(lst_90[j][i])
        tmp.reverse()
        lst_180.append(tmp)

    lst_270 = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(lst_180[j][i])
        tmp.reverse()
        lst_270.append(tmp)

    print("#{}".format(test_case))
    for i in range(N):
        print("".join(lst_90[i][:]), end=' ')
        print("".join(lst_180[i][:]), end=' ')
        print("".join(lst_270[i][:]), end=' ')
        print()
