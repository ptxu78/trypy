#
# 二分查找
# @param n int整型 数组长度
# @param v int整型 查找值
# @param a int整型一维数组 有序数组
# @return int整型
# 详见 https://leetcode-cn.com/problems/binary-search/solution/er-fen-cha-zhao-xiang-jie-by-labuladong/
class Solution:
    def __init__(self):
        self.resu = -1
    # 应对无重复的二分查找
    def binarySearchRec(self,l,r,v,li):
        if l > r:
            return
        else:
            m = (l + r) // 2
            if li[m] > v:
                r = m - 1
                self.binarySearchRec(l,r,v,li)
            elif li[m] < v:
                l = m + 1
                self.binarySearchRec(l,r,v,li)
            else:
                self.resu = m
    # 有重复的二分查找,找左边界
    def binarySearch(self,l,r,v,li):
        while l <= r:
            m = (l + r) // 2
            if v < li[m]:
                r = m - 1
            elif v > li[m]:
                l = m + 1
            else:
                r = m - 1
        if l >= len(li) or li[l] != v:
            self.resu = -1
        else:
            self.resu = l




a = Solution()
a.binarySearch(0,99,100,[2,3,3,4,4,5,5,5,6,6,7,7,9,9,9,10,10,12,14,16,17,18,18,18,19,22,23,23,26,26,26,26,28,28,29,29,29,32,33,35,36,38,39,39,40,41,46,47,47,47,49,50,54,55,55,55,56,57,57,58,58,58,59,61,61,62,62,62,62,63,63,67,67,69,70,70,71,72,74,75,76,79,84,85,85,86,89,92,93,93,93,94,94,95,97,97,97,97,97,99])
print(a.resu)
print(len([2,3,3,4,4,5,5,5,6,6,7,7,9,9,9,10,10,12,14,16,17,18,18,18,19,22,23,23,26]))