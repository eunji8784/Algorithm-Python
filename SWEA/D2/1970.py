T = int(input())
types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for test_case in range(1, T + 1):
    N = int(input())
    res = []

    for tp in types:
        count = 0
        count, N = divmod(N, tp)
        res.append(str(count))

    print("#{}".format(test_case))
    print(" ".join(res))
