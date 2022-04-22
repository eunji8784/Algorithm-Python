import sys
diceList = list(map(int, sys.stdin.readline().split()))
reward = 0

for dice in diceList:
  if diceList.count(dice) == 2:
    reward = 1000 + dice * 100
    break
  elif diceList.count(dice) == 3:
    reward = 10000 + dice * 1000
    break
  else:
    if len(diceList) == len(set(diceList)):
      reward = max(diceList) * 100
      break
    else:
      continue

print(reward)
