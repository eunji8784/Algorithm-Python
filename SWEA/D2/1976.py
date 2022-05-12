T = int(input())

for test_case in range(1, T + 1):
    fh, fm, sh, sm = map(int, input().split())

    res_m = fm + sm
    h = 0
    if res_m > 59:
        h, res_m = divmod(res_m, 60)

    if (fh + sh + h) % 12 == 0:
        res_h = 12
    else:
        res_h = (fh + sh + h) % 12

    print("#{} {} {}".format(test_case, res_h, res_m))
