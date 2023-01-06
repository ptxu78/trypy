# 回溯法 子集树
class Solution:
    def subsets(self, A):
        # write code here
        self.res = []
        self.backtrack([], 0, A)
        return self.res

    def backtrack(self, sol, index, A):
        if index == len(A):
            self.res.append(sol)
            return
        self.backtrack(sol + [A[index]], index + 1, A)
        self.backtrack(sol, index + 1, A)
x = ['A', 'B', 'C', 'D']
a = Solution()
print(a.subsets(x))

    # void Backtrack(int t) {     //t 表示集合 S 的第 t 个元素
    #     if (t > n)
    #         output(x);
    #     else
    #         for (int i = t; i <= n; i++) {      //第t 个元素与其后面的所有元素进行交换位置
    #             swap(x[t], x[i]);
    #             if (constraint(t) && bound(t)){
    #                     backtrack(t + 1);
    #                 }
    #             swap(x[t], x[i]);
    #         }
    # }


x = ['A','B','C','D']
# 递归排列树法 输出数组的全排列
# def backTrack(pt):
#     if pt >= len(x):
#         print(x)
#     else:
#         i = pt
#         while i < len(x):
#             x[i],x[pt] = x[pt],x[i]
#             if True:
#                 backTrack(pt+1)
#             x[i], x[pt] = x[pt], x[i]
#
#             i = i+1

# # 排列树的另一种实现方法
# out = []
# def backTrack(l):
#     if len(out) >= 3:
#         print(out)
#     else:
#         for i in range(len(l)):
#             out.append(l[i])
#             temp = l.pop(i)
#             if True:
#                 backTrack(l)
#             l.insert(i,temp)
#             out.pop()
# backTrack(x)