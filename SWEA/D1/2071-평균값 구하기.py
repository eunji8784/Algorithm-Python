T = int(input())
array = [list(map(int, input().split())) for _ in range(T)]
 
for t in range(T):
  print("#{} {}".format(t+1, round(sum(array[t])/len(array[t]))))
