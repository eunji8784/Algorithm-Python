T = int(input())

for test_case in range(T):
  N = int(input())
  array = [[0] * N for _ in range(N)]

  print("#{}".format(test_case + 1))
  
  for i in range(N):
    array[i][0] = array[i][i] = 1
  
    if i >= 2:
      for j in range(1, i):
        array[i][j] = array[i-1][j-1] + array[i-1][j]

    row = [str(s) for s in array[i][:i+1]]
    print(" ".join(row))
