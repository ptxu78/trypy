## 读入
# n为长, m为宽
n, m = map(int, input().split(' '))
# inMap 原始输入矩阵, 增加边界
inMap = []
inMap.append(list('.'* (m+2)))
for i in range(n):
    inMap.append(list('.' + input() + '.'))
inMap.append(list('.'* (m+2)))

tagCount = 0
# 广度优先 地 标记油井
for i in range(len(inMap)):
    for j in range(len(inMap[0])):
        searchQueue = []
        # 探测到#, 则进入广度优先搜索
        if inMap[i][j] == '#':
            searchQueue.append((i,j))
            inMap[i][j] = str(tagCount)
            # 用先入先出队列辅助广度搜索
            while searchQueue:
                (x, y) = searchQueue.pop(0)
                # 1号方向
                if inMap[x - 1][y - 1] == "#":
                    searchQueue.append((x - 1, y - 1))
                    inMap[x - 1][y - 1] = str(tagCount)
                # 2号方向
                if inMap[x - 1][y] == "#":
                    searchQueue.append((x - 1, y))
                    inMap[x - 1][y] = str(tagCount)
                # 3号方向
                if inMap[x - 1][y + 1] == "#":
                    searchQueue.append((x - 1, y + 1))
                    inMap[x - 1][y + 1] = str(tagCount)
                # 4号方向
                if inMap[x][y - 1] == "#":
                    searchQueue.append((x, y - 1))
                    inMap[x][y - 1] = str(tagCount)
                # 6号方向
                if inMap[x][y + 1] == "#":
                    searchQueue.append((x, y + 1))
                    inMap[x][y + 1] = str(tagCount)
                # 7号方向
                if inMap[x + 1][y - 1] == "#":
                    searchQueue.append((x + 1, y - 1))
                    inMap[x + 1][y - 1] = str(tagCount)
                # 8号方向
                if inMap[x + 1][y] == "#":
                    searchQueue.append((x + 1, y))
                    inMap[x + 1][y] = str(tagCount)
                # 9号方向
                if inMap[x + 1][y + 1] == "#":
                    searchQueue.append((x + 1, y + 1))
                    inMap[x + 1][y + 1] = str(tagCount)

            tagCount = tagCount + 1
print(tagCount)



