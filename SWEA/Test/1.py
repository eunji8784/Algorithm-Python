T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    result = 0

    for i in range(N):
        for j in range(i + 1, N, 1):
            result += array[i] % array[j]
            result += array[j] % array[i]

    print("#{} {}".format(test_case, result))
