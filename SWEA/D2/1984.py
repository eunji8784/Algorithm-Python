T = int(input())

for test_case in range(1, T + 1):
    array = list(map(int, input().split()))

    array.remove(max(array))
    array.remove(min(array))

    res = sum(array) / len(array)

    print("#{} {}".format(test_case, round(res)))
