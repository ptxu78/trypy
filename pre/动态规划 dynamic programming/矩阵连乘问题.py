l = [30, 35, 15, 5, 10, 20, 25]
lenJ = len(l) - 1
#  存储结构初始化
c = []
for i in range(len(l)):
    c.append([0]*len(l))

n = []
for i in range(len(l)):
    n.append([0]*len(l))


# 按步长填充
for step in range(1, lenJ):
    for i in range(1, lenJ-step+1):
        j = i + step
        c[i][j] = c[i][i] + c[i+1][j] + l[i-1]*l[i]*l[j]
        n[i][j] = i

        for k in range(i+1, j):
            isminc = c[i][k] + c[k+1][j] + l[i-1]*l[k]*l[j]
            if isminc < c[i][j]:
                c[i][j] = isminc
                n[i][j] = k


for i in range(lenJ):
    print()



def traceback(i, j):
    if i == j:
        return
    elif i == j - 1:
        print(i,' * ',j)
        return
    else:
        traceback(i,n[i][j])
        traceback(n[i][j]+1,j)
        print(i,'to',n[i][j],' * ',n[i][j]+1,'to',j)
traceback(1,lenJ)

