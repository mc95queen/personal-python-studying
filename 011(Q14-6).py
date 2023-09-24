dic = {}
while True:
    name = input("이름은?").strip()

    if name in dic:
        print("%s의 별명은 %s입니다^^" % (name, dic[name]))
        break

    nickname = input("%s의 별명은? " % name).strip()
    dic[name] = nickname
    print("=" * 15)