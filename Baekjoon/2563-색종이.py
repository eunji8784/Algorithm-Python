import sys
input = sys.stdin.readline

array = [[0] * 100 for _ in range(100)]
n = int(input())

for _ in range(n):
  x1, y1 = map(int, input().split())
  x2, y2 = x1 + 10, y1 + 10
  
  for i in range(x1, x2):
    for j in range(y1, y2):
      array[i][j] = 1

area = 0
for a in array:
  area += sum(a)

print(area)
