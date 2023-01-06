class Solution:
    def LCP(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
    def LCP2(self,strs):
        res = ''
        cmped = strs[0]
        minLen = len(cmped)+1
        for cmp in strs[1::]:
            tmpLen = 0
            for i in range(min(len(cmped),len(cmp))):
                if cmped[i] == cmp[i]:
                    tmpLen+=1
            if tmpLen < minLen:
                minLen = tmpLen
        return cmped[0:minLen]
s = Solution()
print(s.LCP2(['pity','pityqaq','pipi']))