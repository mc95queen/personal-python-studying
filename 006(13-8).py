hor = 5
ver = 5
li = []

# 2차원 리스트 초기화
for i in range(hor):
    hor_li = []
    for j in range(ver):
        hor_li.append(0)
    li.append(hor_li)

# 1행의 1열, 3열, 5열을 1로 설정
li[0][0] = 1
li[0][2] = 1
li[0][4] = 1

# 나머지 행 채우기
for i in range(1, hor_li):
    for j in range(1, ver - 1):
        li[i][j] = li[i-1][j-1] + li[i-1][j+1]

# 행렬 출력
for row in li:
    print(row)