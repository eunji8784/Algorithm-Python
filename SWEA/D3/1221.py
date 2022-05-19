T = int(input())
num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1, T + 1):
    t, N = input().split()
    array = list(input().split())
    result = []

    for num in num_lst:
        i = array.count(num)
        if i > 0:
            for _ in range(i):
                result.append(num)

    print(t)
    print(" ".join(result))
