# solution 1
n = int(input())

for i in range(n + 1):
  if i == 0:
    result = 1
  else:
    result *= 2
  print(result, end = ' ')
  
# solution 2
# n = int(input())

# for i in range(n + 1):
#   print(2 ** i, end = ' ')
