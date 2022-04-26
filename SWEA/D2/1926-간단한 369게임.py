N = int(input())
list369 = ['3', '6', '9']

for n in range(1, N + 1):
  digit = list(str(n))
  exsisting369 = False
  
  for d in digit:
    if d in list369:
      print('-', end = '')
      exsisting369 = True

  if exsisting369:
    print(end = ' ')
  else:
    print(n, end = ' ')
