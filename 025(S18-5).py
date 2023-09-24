class Height:
    def __init__(self, surname, heightvalue):
        self.surname = surname
        self.heightvalue = heightvalue
    def __lt__(self, other):
        return self.heightvalue > other.heightvalue
    
def minsearch(sav):
    poor = sav[0]
    for now in sav:
        if now < poor: now = poor
    return poor

saving = []
for i in range(5):
    surname, heightvalue = input().split()
    surname = str(surname)
    heightvalue = int(heightvalue)
    saving.append(Height(surname, heightvalue))

poor = minsearch(saving)
print("%s %d" % (poor.surname, poor.heightvalue))