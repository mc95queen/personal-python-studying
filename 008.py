a = int(input())

def name(n):
    if n < 1: return
    name(n-1)
    print("recursive")

name(a)