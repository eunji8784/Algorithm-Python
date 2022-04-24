import sys
n = int(sys.stdin.readline())
wordList = [sys.stdin.readline().rstrip() for _ in range(n)]

wordList1 = list(set(wordList))
wordList1.sort()
for word in sorted(wordList1, key=len):
  print(word)
