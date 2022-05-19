T = 10

for test_case in range(1, T + 1):
    N, password = input().split()
    password = list(password)
    N = int(N)

    status = True
    while status:
        for i in range(len(password) - 1):
            status = False
            if password[i] == password[i + 1]:
                password.pop(i)
                password.pop(i)
                status = True
                break

    print("#{} {}".format(test_case, "".join(password)))
