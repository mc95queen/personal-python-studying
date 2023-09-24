class Person:
    def __init__(self, surname, heightvalue, weightvalue):
        self.surname = surname
        self.heightvalue = heightvalue
        self.weightvalue = weightvalue
    def __lt__(self, other):
        return self.weightvalue > other.weightvalue
    def prn(self):
        print("%s %d %.1f" % (self.surname, self.heightvalue, self.weightvalue))

def inp(st):
    for i in range(5):
        sur, height, weight = input().split()
        st.append(Person(sur, int(height), float(weight)))

def outp(st):
    for s in st: s.prn()
    print()

def name(self):
    return self.surname

stu = []
inp(stu)
stu.sort()
outp(stu)
stu.sort(key = name)
outp(stu)