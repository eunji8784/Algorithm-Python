T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    jak = hol = 0

    # 조건을 만족할 수 있는지 검사
    for i in range(N):
        if array[i] % 2 == 0:
            jak += 1
        else:
            hol += 1

    if N % 2 == 0:
        if jak == N // 2 and hol == N // 2:
            result = 0
        else:
            result = -1
    else:
        if jak == N // 2 and hol == (N // 2) + 1:
            result = 0
        elif jak == (N // 2) + 1 and hol == N // 2:
            result = 0
        else:
            result = -1

    if result != -1:
        tmp = 1
        while tmp != 0:
            tmp = 0
            for i in range(N - 2):
                if array[i] % 2 == 0: # 짝수
                    if array[i + 1] % 2 != 0: # 홀수
                        continue
                    else: # 짝수
                        if array[i + 2] % 2 != 0: # 홀수
                            array[i + 1], array[i + 2] = array[i + 2], array[i + 1]
                            tmp += 1
                            result += 1

                else: # 홀수
                    if array[i + 1] % 2 == 0: # 짝수
                        continue
                    else: # 홀수
                        if array[i + 2] % 2 == 0: # 짝수
                            array[i + 1], array[i + 2] = array[i + 2], array[i + 1]
                            tmp += 1
                            result += 1

    print("#{} {}".format(test_case, result))
