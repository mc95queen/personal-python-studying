a = int(input())
dic = {}

for i in range(a):
    nation, capital = input().split()

    dic[nation] = capital

inputnation = input().strip()

if inputnation in dic:
    print(dic[inputnation])
else:
    print("Unknown Country")