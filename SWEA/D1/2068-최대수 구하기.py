T = int(input())
array = []

for _ in range(T):
  numList = list(map(int, input().split()))
  array.append(numList)

t = 1
for a in array:
  print("#{} {}".format(t, max(a)))
  t += 1
