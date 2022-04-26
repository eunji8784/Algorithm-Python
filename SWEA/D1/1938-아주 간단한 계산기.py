import math
a, b = map(int, input().split())

if a < b:
  a, b = b, a
  
print(a + b)
print(a - b)
print(a * b)
print(math.trunc(a / b))
