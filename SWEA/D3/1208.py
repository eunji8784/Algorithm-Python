T = 10

for test_case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().split()))
    res = 0

    for _ in range(N):
        max_idx = array.index(max(array))
        min_idx = array.index(min(array))
        array[max_idx] -= 1
        array[min_idx] += 1

        res = max(array) - min(array)

        if res <= 1:
            break

    print("#{} {}".format(test_case, res))
