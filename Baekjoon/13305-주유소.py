cityNum = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min = price[0]
result = min * distance[0]
j = 1
for i in price[1:-1]:
  if i < min:
    min = i
  result += min * distance[j]
  j += 1

print(result)
