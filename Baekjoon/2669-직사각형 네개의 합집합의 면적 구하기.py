import sys

array = [[0] * 100 for _ in range(100)]

for _ in range(4):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  
  for i in range(x1, x2):
    for j in range(y1, y2):
      array[i][j] = 1

area = 0
for a in array:
  area += sum(a)

print(area)
