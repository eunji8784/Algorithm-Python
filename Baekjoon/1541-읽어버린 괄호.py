exps = input()
exp_list = exps.split('-')
n = 0
list = []

for exp in exp_list:
  if "+" in exp:
    for i in exp.split('+'):
      i = int(i)
      n += i
    list.append(n)
    n = 0
  else:
    list.append(int(exp))

result = list[0]
for i in list[1:]:
  result -= i

print(result)
