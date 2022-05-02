import sys
input = sys.stdin.readline

student_num = int(input())
num_list = list(map(int, input().split()))

array = []
for i in range(student_num):
    array.insert(i - num_list[i], str(i + 1))

print(" ".join(array))
