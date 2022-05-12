T = int(input())

for test_case in range(1, T + 1):
    array = [input().split() for _ in range(9)]
    ans = 1

    if ans:
        # 가로 줄 검사
        for a in array:
            if len(set(a)) != 9:
                ans = 0
                break

        # 세로 줄 검사
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(array[j][i])
            if len(set(tmp)) != 9:
                ans = 0
                break

        # 3 X 3 격자 검사
        for i in range(9):
            if i % 3 == 0:
                if len(set(tmp)) != 9:
                    ans = 0
                    break
                else:
                    tmp = []
            for j in range(3):
                tmp.append(array[j][i])

        for i in range(9):
            if i % 3 == 0:
                if len(set(tmp)) != 9:
                    ans = 0
                    break
                else:
                    tmp = []
            for j in range(3, 6):
                tmp.append(array[j][i])

        for i in range(9):
            if i % 3 == 0:
                if len(set(tmp)) != 9:
                    ans = 0
                    break
                else:
                    tmp = []
            for j in range(6, 9):
                tmp.append(array[j][i])

    print("#{} {}".format(test_case, ans))
