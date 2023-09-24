def squareplus(n):
    if n <= 0: return 0
    return squareplus(n // 10) + ((n % 10) * (n % 10))

n = int(input())
print(squareplus(n))