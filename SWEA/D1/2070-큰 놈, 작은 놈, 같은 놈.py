T = int(input())
 
for t in range(T):
  a, b = map(int, input().split())
  if a > b:
    answer = ">"
  elif a < b:
    answer = "<"
  else:
    answer = "="
  print("#{} {}".format(t+1, answer))

# solution 2  
# T = int(input())
# array = []

# for _ in range(T):
#   a, b = map(int, input().split())
#   array.append([a, b])

# t = 1
# for a, b in array:
#   if a > b:
#     answer = ">"
#   elif a < b:
#     answer = "<"
#   else:
#     answer = "="
#   print("#{} {}".format(t, answer))
#   t += 1
