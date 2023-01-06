# coding=utf-8
# LCS: 最长公共子序列.

s = "abcda"
dp = []
lenS = int(len(s + 1))
# 矩阵初始化为1
for i in range(lenS):
    temList = []
    for j in range(lenS):
        temList.append(1)
    dp.append(temList)

# 动态规划 dynamic programming
for i in range(1, lenS + 1):
    for j in range(1, lenS + 1):
        # 当无重复字符时
        if s[j - 1] not in s[i - 1, j]:
            dp[i][j] = dp[i][j - 1] + 1
        # 有重复字符时
        else:
            # 求分段的最大值
            dp[i][j] = max(dp[i, j - 1], s[::-1].index(s[j - 1]))
