# https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode/
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        returns = ''
        l = 0
        r = len(s)-1
        self.isC(1,s)
        # while(l <= r):
        #     m = (l+r) // 2

    def isC(self,lenC,s) -> bool:
        hashT = {}
        listT = []
        for i in range(len(s) - lenC + 1):
            listT.append(s[i:i+lenC])

a = Solution()
a.longestDupSubstring('abcba')