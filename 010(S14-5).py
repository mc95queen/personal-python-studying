dic = { "Pokemon" : 1, "Digimon" : 2, "Yugioh" : 3}

st = input().strip()

if dic[st] == 1:
    print("Pikachu")
elif dic[st] == 2:
    print("Agumon")
elif dic[st] == 3:
    print("Black Magician")
else:
    print("I don't know")