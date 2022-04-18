import sys
n, k = map(int, input().split())
coin_types = [int(sys.stdin.readline()) for i in range(n)]
count = 0

coin_types.sort(reverse = True)

for coin in coin_types:
  count += k // coin
  k %= coin

print(count)
