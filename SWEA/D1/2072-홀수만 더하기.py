n = int(input())

array = []
for _ in range(n):
  numList = list(map(int, input().split()))
  array.append(numList)

t = 1
for i in array:
  sum = 0
  for j in range(len(i)):
    if i[j] % 2 == 1:
      sum += i[j]
  print("#"+ str(t), sum)
  t += 1
