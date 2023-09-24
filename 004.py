a = [95, 75, 85, 100, 50]

for i in range(4):
    for j in range(i + 1, 5):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            

for i in range(5):
    print(a[i], end = ' ')

