class COM:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return COM(x, y)
    def __truediv__(self, divisor):
        return COM(self.x / divisor, self.y / divisor)
    
x, y = map(float, input().split())
p1 = COM(x, y)
x, y = map(float, input().split())
p2 = COM(x, y)
x, y = map(float, input().split())
p3 = COM(x, y)
p4 = p1 + p2 + p3

p4 /= 3

print("(%.1f, %.1f)" % (p4.x, p4.y))