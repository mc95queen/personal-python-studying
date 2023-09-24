a = int(input())

init_alpha = ord('A')

for i in range(1, a+1):
    for j in range(1, i+1):
        print(chr(init_alpha), end = '')
        init_alpha += 1
    print()