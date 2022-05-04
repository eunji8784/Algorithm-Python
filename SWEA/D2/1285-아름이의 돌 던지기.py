T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    location = list(map(int, input().split()))
    min_value = abs(location[0])
    count = 0

    for i in location:
        if abs(i) < min_value:
            min_value = abs(i)
        elif abs(i) == min_value:
            count += 1
        else:
            continue

    print("#{} {} {}".format(test_case, min_value, count))
