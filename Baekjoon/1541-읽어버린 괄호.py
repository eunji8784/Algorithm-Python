exps = input()
exp_list = exps.split('-')
n = 0
list = []

for exp in exp_list:
  if "+" in exp:
    for str in exp.split('+'):
      num = int(str)
      n += num
    list.append(n)
    n = 0
  else:
    list.append(int(exp))

result = list[0]
for i in list[1:]:
  result -= i

print(result)

# Pythonic하게 바꾼 코드
# exp = [sum(map(int, x.split('+'))) for x in input().split('-')]
# print(exp[0] - sum(exp[1:]))
