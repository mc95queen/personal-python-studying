class StudentInfo:
    def __init__(self, name, kor, eng):
        self.name = name
        self.kor = kor
        self.eng = eng
    def prn(self):
        print("%s %d %d" % (self.name, self.kor, self.eng))

name, kor, eng = input().split()
st1 = StudentInfo(name, int(kor), int(eng))
name, kor, eng = input().split()
st2 = StudentInfo(name, int(kor), int(eng))
average =((st1.kor + st2.kor)/2, (st1.eng + st2.eng)/2)

st1.prn()
st2.prn()
print(average)
