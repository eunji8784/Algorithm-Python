T = int(input())
array = [2, 3, 5, 7, 11]

for test_case in range(1, T + 1):
    N = int(input())
    result = []

    while N not in array:
        for i in array:
            if N % i == 0:
                result.append(i)
                N //= i
                break

    result.append(N)

    r = []
    for j in range(len(array)):
        r.append(str(result.count(array[j])))

    print("#{} {}".format(test_case, " ".join(r)))
