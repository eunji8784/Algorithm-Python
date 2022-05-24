T = int(input())

for test_case in range(1, T + 1):
    str = list(input())
    H = int(input())
    location = list(map(int, input().split()))
    location.sort(reverse=True)

    for i in range(H):
        str.insert(location[i], '-')

    print("#{} {}".format(test_case, "".join(str)))
