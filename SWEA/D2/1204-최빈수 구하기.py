from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    test_case_num = int(input())
    score_list = list(map(int, input().split()))

    score_list.sort(reverse=True)
    array = Counter(score_list).most_common()

    print("#{} {}".format(test_case_num, array[0][0]))
