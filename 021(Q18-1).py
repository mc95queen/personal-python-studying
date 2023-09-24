class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("느그이름")
age = int(input("느그나이"))
st = Student(name, age)

print("느그이름 %s" % st.name, end = ' ')
print("느그나이 %d" % st.age)