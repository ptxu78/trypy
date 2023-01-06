## 输入
n = int(input())
inStr = input()

## 分单核与双核, 穷举对称子串
maxPtr = n - 1
maxSubLen = 0
for core in range(len(inStr)):
    # 单核情况
    step = 1
    subLen = 1
    while core - step >= 0 and core + step <= maxPtr and inStr[core - step] == inStr[core + step]:
        subLen = subLen + 2
        step = step + 1
    if subLen > maxSubLen:
        maxSubLen = subLen

    # 双核情况

    if core + 1 <= maxPtr and inStr[core] == inStr[core+1]:
        coreSecond = core + 1
        step = 1
        subLen = 2
        while core - step >= 0 and coreSecond + step <= maxPtr and inStr[core - step] == inStr[coreSecond + step]:
            subLen = subLen + 2
            step = step + 1
        if subLen > maxSubLen:
            maxSubLen = subLen
print(maxSubLen)