T = 10

for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    count = 0

    for i in range(2, N - 2):
        tmp = []
        tmp.extend(array[i - 2:i])
        tmp.extend(array[i + 1:i + 3])

        if max(tmp) < array[i]:
            count += array[i] - max(tmp)

    print("#{} {}".format(test_case, count))
