students = input().split()
dic = {}

for student in students:
    if student in dic:
        dic[student] += 1
    else:
        dic[student] = 1

maxi = 0
for student, cnt in dic.items():
    if maxi < cnt:
        leader, maxi = student, cnt

print("반장은 " + leader + "입니다.")
print(leader+ "가 받은 표는" + str(cnt)+"표입니다")

