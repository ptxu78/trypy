a = "aAsmr3idd4bgs7Dlsf9eAAF"
# 1 大小写
# 字符串是无法修改的,将字符串转成list方便大小写修改
a = list(a)
for i in range(len(a)): # range学过吗? len学过吗?
    if 'a' <= a[i] <= 'z':
        a[i] = a[i].upper() # 讲一个小写字符变成大写的
    elif 'A' <= a[i] <= 'Z':
        a[i] = a[i].lower()

# 将list组合成字符串用join方法,自行百度吧
a = ''.join(a)
print(a)

# 2 取出数组
numList = []
for i in range(len(a)):
    if '0' <= a[i] <= '9':
        numList.append(a[i]) # append学过吗
numList = ''.join(numList)
print(numList)

# 3 统计
staDic = {} # 字典学过吗?
for i in range(len(a)):
    if a[i] in staDic:
        staDic[a[i]] += 1
    else:
        staDic[a[i]] = 1
print(staDic)

# 4去重
a = list(a)
isFirst = True
i = 0 # 表示当前正在检测字母的序号

while i < len(a):
    if 'a' == a[i] or 'A' == a[i]:
        if isFirst == True:
            isFirst = False
        else:
            a.pop(i)
            continue
    i += 1

a = ''.join(a)
print(a)
