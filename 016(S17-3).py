def summ(n):
    if n < 1: return 0
    return n + summ(n-1)

n = int(input())
print(summ(n))