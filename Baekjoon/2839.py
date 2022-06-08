arr = [1, 2, 4, 7]
N = int(input())
count = 0

while N > 0:

    if N % 5 == 0:
        count += N // 5
        break

    N -= 3
    count += 1

    if N in arr:
        count = -1
        break

print(count)
