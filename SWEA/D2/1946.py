for test_case in range(1, T + 1):
    N = int(input())
    array = []
    count = 0

    for i in range(1, N + 1):
        C, K = input().split()

        for _ in range(int(K)):
            array.append(C)

            if (len(array) - count) % 10 == 0:
                array.append('\n')
                count += 1

    if array[-1] == '\n':
        array.pop()

    print("#{}".format(test_case))
    print("".join(array))
