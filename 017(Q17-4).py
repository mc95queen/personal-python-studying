def output():
    for i in range(1, n+1):
        print(arr[i], end = ' ')
    print()

def dice(step):
    if step > n:
        output()
        return
    for i in range(1, 7):
        arr[step] = i
        dice(step + 1)

n = int(input())
arr = [0 for i in range(n+1)]
dice(1)