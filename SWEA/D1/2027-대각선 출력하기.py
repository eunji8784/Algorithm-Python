array = ['+' for _ in range(5)]

for i in range(len(array)):
  array[i] = '#'
  print("".join(array))
  array[i] = '+'
