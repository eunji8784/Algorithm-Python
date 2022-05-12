T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    A = W * P
    B = 0

    if W > R:
        B = Q + (W - R) * S
    else:
        B = Q

    print("#{} {}".format(test_case, min(A, B)))
