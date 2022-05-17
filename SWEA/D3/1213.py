T = 10

for test_case in range(1, T + 1):
    N = int(input())
    find = input()
    sentence = input()

    print("#{} {}".format(N, sentence.count(find)))
