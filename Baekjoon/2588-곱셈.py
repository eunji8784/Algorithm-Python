import sys
a = int(sys.stdin.readline())
b = sys.stdin.readline().rstrip()
listB = [int(i) for i in b]

for i in reversed(listB):
  print(i*a)

print(a*int(b))
