T = 10

for test_case in range(1, T + 1):
    N = int(input())
    array = [list(map(int, input().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        one = False
        for j in range(N):
            if array[j][i] == 1:
                one = True
            if one and array[j][i] == 2:
                count += 1
                one = False

    print("#{} {}".format(test_case, count))
