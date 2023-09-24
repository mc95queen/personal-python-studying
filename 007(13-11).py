import math

a = int(input())


for i in range(1, a+1):
    for j in range(0, a+1):
       if a-i-j < 0:
           break
       print(int((math.factorial(a-i))/((math.factorial(j))*(math.factorial(a-i-j)))), end = ' ')
    print()