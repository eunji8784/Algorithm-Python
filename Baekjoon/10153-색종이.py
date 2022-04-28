import sys
input = sys.stdin.readline

array = [[0] * 1001 for _ in range(1001)] 

N = int(input())

for n in range(1, N + 1):
  x, y, width, height = map(int, input().split())
  
  for i in range(x, x + width):
    array[i][y:(y + height)] = [n] * height

result_list = [0 for _ in range(N)]
for i in range(len(array)):
  for j in range(len(array[i])):
    if array[i][j]:
      result_list[array[i][j] - 1] += 1

for result in result_list:
  print(result)
