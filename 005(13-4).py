li = input().split()

a = len(li)

analyzedlist = []

for i in range(0, a):
    analyzedlist.append(int(li[i]) // 10)

analyzedlist.sort(reverse = True)

print(analyzedlist)

for j in range(10, 5, -1):
    num = analyzedlist.count(j)
    print(j*10, ':', num, 'person')
