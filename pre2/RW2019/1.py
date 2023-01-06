# 测试数据
# 3 2
# 11 12 20

# 测试数据2
# 5 4
# 1001 0042 0165 1999 0605

# 输入
lenList, lenNum = map(int, input().split(' '))

# 将每个数都转成 元组:按位存储的字符
myList = list(map(tuple,input().split(' ')))

# 按照从数字最低位到最高位, 统计词频
wei = lenNum - 1
while  wei >= 0:
    # 统计词频字典
    mydict = {}
    for i in range(lenList):
        key = myList[i][wei]
        mydict[key] = mydict.get(key,0) + 1

    # 找字频最多的最小数字
    maxValue = max(mydict.values())
    outputKey = 10
    for key, value in mydict.items():
        if value == maxValue:
            if int(key) < outputKey:
                outputKey = int(key)
    print(outputKey)
    wei = wei - 1

