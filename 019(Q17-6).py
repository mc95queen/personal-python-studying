def plusing(n):
    if n <= 0: return 0
    return plusing(n // 10) + (n % 10)

n = int(input())
print(plusing(n))