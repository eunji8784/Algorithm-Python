T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    total_grade = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        total_grade.append(a * 0.35 + b * 0.43 + c * 0.2)

    k_score = total_grade[K - 1]
    total_grade.sort(reverse=True)

    idx = total_grade.index(k_score)

    ratio = N // 10
    i = j = 0
    while i != len(total_grade):
        for _ in range(ratio):
            total_grade[i] = grade[j]
            i += 1
        j += 1

    print("#{} {}".format(test_case, total_grade[idx]))
