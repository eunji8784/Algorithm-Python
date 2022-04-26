T = int(input())
array = [[*map(int, input().split())] for _ in range(T)]

t = 1
for a, b in array:
  if a > b:
    answer = ">"
  elif a < b:
    answer = "<"
  else:
    answer = "="
  print("#{} {}".format(t, answer))
  t += 1
