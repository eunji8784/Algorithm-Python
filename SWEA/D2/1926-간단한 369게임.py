N = int(input())
clap = ['3', '6', '9']

for n in range(1, N + 1):
  digit = list(str(n))
  isClap = False
  
  for d in digit:
    if d in clap:
      print('-', end = '')
      isClap = True

  if isClap:
    print(end = ' ')
  else:
    print(n, end = ' ')
