T = int(input())

for test_case in range(1, T + 1):
    word = input()
    res = 0

    r_word = list(reversed(word))

    if word == "".join(r_word):
        res = 1

    print("#{} {}".format(test_case, res))
