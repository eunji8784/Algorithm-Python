T = int(input())

for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())
    min_v = -1

    for R in range(1, N + 1):
        C = 1
        while R * C <= N:
            tmp = A * abs(R - C) + B * (N - R * C)
            if min_v == -1:
                min_v = tmp
            else:
                min_v = min(min_v, tmp)
            C += 1

    print("#{} {}".format(test_case, min_v))
