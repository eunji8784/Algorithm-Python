T = int(input())

for test_case in range(1, T + 1):
    origin = list(input())
    count = 0

    init = []
    for _ in range(len(origin)):
        init.append('0')

    idx = 0
    while origin != init:
        
        idx = origin[idx:].index('1') + idx
        init[idx:] = ['1' for _ in range(len(origin) - idx)]
        count += 1
        
        if origin[idx:].count('0') > 0:
            idx = origin[idx:].index('0') + idx
            init[idx:] = ['0' for _ in range(len(origin) - idx)]
            count += 1

    print("#{} {}".format(test_case, count))
