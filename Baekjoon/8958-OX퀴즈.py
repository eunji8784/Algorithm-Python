import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  str = input()
  count, sum = 0, 0
  
  for i in range(len(str)):
    if str[i] == 'O':
      count += 1
      sum += count
    else:
      count = 0
      
  print(sum)
