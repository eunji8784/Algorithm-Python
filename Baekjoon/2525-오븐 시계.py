import sys
h, m = map(int, sys.stdin.readline().split())
time = int(sys.stdin.readline())

x = h * 60 + m + time
print(x // 60 % 24, x % 60)
