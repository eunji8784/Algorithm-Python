T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    speed = 0
    m = 0

    for _ in range(N):
        array = input().split()

        if len(array) == 1 and int(array[0]) == 0:
            m += speed
            continue
        else:
            c, s = map(int, array)

        if c == 1:
            speed += s
        else:
            if speed > s:
                speed -= s
            else:
                speed = 0

        m += speed

    print("#{} {}".format(test_case, m))
