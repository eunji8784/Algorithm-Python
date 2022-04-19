n = int(input())
time = []

for _ in range(n):
  start, end = map(int, input().split())
  time.append([start, end])

# end 기준으로 오름차순 정렬, end가 같을 경우에는 start 기준으로 오름차순 정렬
time.sort(key=lambda x: (x[1], x[0]))

last = 0
count = 0

for i, j in time:
  if i >= last:
    last = j
    count += 1

print(count)
