T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    profit = 0

    max_v = array[-1]
    for i in range(N - 1, -1, -1):
        if array[i] > max_v:
            max_v = array[i]
        profit += max_v - array[i]

    print("#{} {}".format(test_case, profit))
