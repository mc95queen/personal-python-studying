students = input().split()
dic = {}
count = int(input())

for student in students:
    if student in dic:
        dic[student] += 1
    else:
        dic[student] = 1

for student in dic:
    if dic[student] == count:
        print(student)