class person:
    def __init__(self, name, school, grade):
        self.name = name
        self.school = school
        self.grade = grade

name = input().strip()
school = input().strip()
grade = input().strip()

per = person(name, school, grade)

print("Name :", per.name)
print("School :", per.school)
print("Grade :", per.grade)