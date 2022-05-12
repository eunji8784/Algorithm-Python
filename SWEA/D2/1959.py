T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    res = []

    if len(A) > len(B):
        L = A
        S = B
    else:
        L = B
        S = A

    for i in range(len(L) - len(S) + 1):
        num = 0
        for j in range(len(S)):
            num += S[j] * L[i]
            i += 1
        res.append(num)

    print("#{} {}".format(test_case, max(res)))
