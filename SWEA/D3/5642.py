T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    sum_v = 0
    max_v = array[0]

    for i in range(N):
        sum_v += array[i]

        if sum_v > max_v:
            max_v = sum_v

        if sum_v < 0:
            sum_v = 0

    print("#{} {}".format(test_case, max_v))
