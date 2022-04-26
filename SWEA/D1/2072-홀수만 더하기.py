# n = int(input())

# array = []
# for _ in range(n):
#   numList = list(map(int, input().split()))
#   array.append(numList)

# t = 1
# for i in array:
#   sum = 0
#   for j in range(len(i)):
#     if i[j] % 2 == 1:
#       sum += i[j]
#   print("#"+ str(t), sum)
#   t += 1

T = int(input())
array = [list(map(int, input().split())) for _ in range(T)]

for t in range(T):
  sum = 0
  for i in array[t]:
    if i % 2 == 1:
      sum += i
  print("#{} {}".format(t + 1, sum))
