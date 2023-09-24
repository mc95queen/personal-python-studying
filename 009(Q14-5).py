dic = { "사과" : 1, "배" : 2}
dic["포도"] = 3

st = input("문자열을 입력하세요: ").strip()

if st in dic:
    print("%d번" % dic[st])
else:
    print("0번")