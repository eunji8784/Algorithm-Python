T = 10

for test_case in range(1, T + 1):
    N = int(input())
    origin = list(input().split())
    M = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            idx = int(command[i + 1])
            num = int(command[i + 2])
            for _ in range(num):
                origin.insert(idx, command[i + 3])
                i += 1
                idx += 1

    print("#{} {}".format(test_case, " ".join(origin[:10])))
