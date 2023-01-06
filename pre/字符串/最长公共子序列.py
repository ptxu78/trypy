# longest common subsequence
# @param s1 string字符串 the string
# @param s2 string字符串 the string
# @return string字符串

class Solution:
    def LCS(self, s1, s2):
        # 初始化矩阵
        m = len(s1)
        n = len(s2)
        if m == 0 or n == 0:
            return -1
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        # 构造矩阵
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # 边界条件
        if dp[m][n] == 0:
            return -1

        # 找结果
        i, j = m, n
        res = []
        while i and j:
            if s1[i - 1] == s2[j - 1]:
                res.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        res = ''.join(reversed(res))

        return res
a = Solution()
print(a.LCS("1A2C3D4B56","B1D23CA45B6A"))