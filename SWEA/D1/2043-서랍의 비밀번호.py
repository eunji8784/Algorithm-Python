P, K = map(int, input().split())
count = 0

while P >= K:
  K += 1
  count += 1

print(count)
