a = ['A','B','C','B','D','A',"B"]
b = ['B','D','C','A','B','A']
lenMax = max(len(a), len(b))

c = []
for i in range(len(a)+1):
    c.append([0]*(len(b)+1))

mode = []
for i in range(len(a)+1):
    mode.append([0]*(len(b)+1))

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            c[i][j] = c[i-1][j-1] + 1
            mode[i][j] = 1
        else:
            c[i][j] = c[i-1][j]
            mode[i][j] = 2
            if c[i][j-1] > c[i-1][j]:
                c[i][j] = c[i][j-1]
                mode[i][j] = 3
LCSstr = []
i = len(a)
j = len(b)
for k in range(c[len(a)][len(b)]):
    if mode[i][j] == 1:
        LCSstr.append(a[i-1])
        i = i-1
        j = j-1
    elif mode[i][j] ==2:
        LCSstr.append(a[i-1])
        i = i-1
    elif mode[i][j] ==3:
        LCSstr.append(b[i-1])
        j = j-1
LCSstr.reverse()
print(LCSstr)
