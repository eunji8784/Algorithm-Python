T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    lst.sort()

    res = [str(i) for i in lst]

    print("#{} {}".format(test_case, " ".join(res)))
