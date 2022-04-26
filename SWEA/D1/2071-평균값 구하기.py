T = int(input())

for t in range(T):
  numList = list(map(int, input().split()))
  print("#{} {}".format(t+1, round(sum(numList)/len(numList))))
