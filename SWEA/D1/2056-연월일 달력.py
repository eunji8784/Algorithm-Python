T = int(input())
d31 = [1, 3, 5, 7, 8, 10, 12]
d30 = [4, 6, 9, 11]

for t in range(T):
  str = input()
  y = str[:4]
  m = str[4:6]
  d = str[6:]
  array = [y, m, d]
  result = "/".join(array)
  
  if int(m) not in range(1, 13):
    result = -1
  else:
    if int(m) in d31:
      if int(d) not in range(1, 31):
        result = -1
    elif int(m) in d30:
      if int(d) not in range(1, 30):
        result = -1
    else:
      if int(d) not in range(1, 29):
        result = -1
    
  print("#{} {}".format(t + 1, result))
