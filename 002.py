a  = int(input())

for i in range(1, a+1):
    st1 = " " * (i-1) + "*" * (a+1-i)
    if i == 1:
        stother1 = ""
    else:
        stother1 = "*"
        st1 = " " * (i-2) + "*" * (a+1-i)
    print(stother1 + st1)


for j in range(1, a+1):
    st2 = "*" * (j-1) + " " * (a+1-j)
    if j == 1:
        stother2 = ""
    else:
        stother2 = "*"
        st2 = "*" * (j-1) + " " * (a-j)
    print(st2 + stother2)