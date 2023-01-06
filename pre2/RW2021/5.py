# 输入 bei:被子 xing:行李箱
stuNum, beiNum, xingNum = map(int, input().split(' '))
# 用嵌套的字典存学生的喜好
stuDict = {}
for i in range(stuNum):
    inputLine = list(map(int, input().split(' ')))
    beiSet = set(inputLine[2: 2 + inputLine[0]])
    xingSet = set(inputLine[2 + inputLine[0]:])

    likeDict = {}
    likeDict["bei"] = beiSet
    likeDict["xing"] = xingSet

    stuDict[i] = likeDict

# 回溯法求最优解, 生成组合树
stuList = list(range(stuNum))
beiList = list(range(1, beiNum+1))
xingList = list(range(1, xingNum+1))
giveList = []


def backTrack(stuList, beiList, xingList, give):
    if beiList == [] or xingList == [] or stuList == []:
        giveList.append(give)
        return

    else:
        for s in stuList:
            for bv in stuDict[s]["bei"]:
                for xv in stuDict[s]["xing"]:
                    if bv in beiList and xv in xingList:
                        stuList.remove(s)
                        beiList.remove(bv)
                        xingList.remove(xv)

                        backTrack(stuList, beiList, xingList, give + 1)

                        stuList.append(s)
                        stuList.sort()
                        beiList.append(bv)
                        xingList.append(xv)

backTrack(stuList, beiList, xingList, 0)
print(max(giveList))
