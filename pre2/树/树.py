import copy
class treeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
# 构造树
def cons(ptr):
    if ptr < len(arr) and arr[ptr] != 'N':
        newNode = treeNode(arr[ptr])
        newNode.left = cons(2 * ptr + 1)
        newNode.right = cons(2 * ptr + 2)
        return newNode
    else:
        return None
# 画树
def draw(root):
    queueQ = [root]
    level = 0
    while queueQ:
        level +=1
        printList = []
        for i in range(len(queueQ)):
            nowNode = queueQ.pop(0)
            if  nowNode != 'N':
                printList.append(nowNode.val)
                if nowNode.left == None:
                    queueQ.append('N')
                else:
                    queueQ.append(nowNode.left)
                if nowNode.right == None:
                    queueQ.append('N')
                else:
                    queueQ.append(nowNode.right)
            else:
                printList.append(nowNode)
        print('level', level, printList)

class Solution:
    # 完全二叉树 广度优先
    def isCBT(self,root):
        queue = [root]
        IsCBT = True
        while queue:
            tmpNode = queue.pop(0)
            if tmpNode.left and tmpNode.right:
                queue.append(tmpNode.left)
                queue.append(tmpNode.right)
            elif not tmpNode.left and tmpNode.right:
                IsCBT = False
            elif tmpNode.left and not tmpNode.right:
                queue.append(tmpNode.left)
                break
            else:
                break
        for i in queue:
            if i.left or i.right:
                IsCBT = False
        return IsCBT
    # 二叉搜索树 二叉排序树 深度优先
    def isBST(self,tree):
        stack = []
        pre = 0
        while(stack or tree):
            if tree:
                stack.append(tree)
                tree = tree.left
            else:
                tree = stack.pop()
                if pre <= tree.val:
                    pre = tree.val
                else:
                    return False
                tree = tree.right
        return True
    #
    def preOrderTraverse(self,tree):
        if tree ==None:
            return
        else:
            print(tree.val)
            self.preOrderTraverse(tree.left)
            self.preOrderTraverse(tree.right)
    # 非递归
    def inOrderTraverseNoReduce(self,tree):
        stack = []
        while stack or tree :
            if tree:
                stack.append(tree)
                tree = tree.left
            else:
                tree = stack.pop()
                print(tree.val)
                tree = tree.right
    # 层次遍历 带level的广度优先
    def levelTraverse(self,tree):
        queue = [tree]
        levelTraverseList = []
        while queue:
            thisLevelList = []
            for i in range(len(queue)):
                tmpTree = queue.pop(0)
                thisLevelList.append(tmpTree.val)
                if tmpTree.left:
                    queue.append(tmpTree.left)
                if tmpTree.right:
                    queue.append(tmpTree.right)
            levelTraverseList.append(thisLevelList)
        return levelTraverseList
    # 找到路径
    findPathStack = []
    findPathAns = []
    def findPath(self,tree,unit):
        if not tree:
            return
        else:
            self.findPathStack.append(tree.val)
            if tree.val == unit:
                self.findPathAns.append(copy.deepcopy(self.findPathStack))
            self.findPath(tree.left,unit)
            self.findPath(tree.right,unit)
            self.findPathStack.pop()


arr = [1,2,3,4,9,5,6,7,8]
treeN = cons(0)

draw(treeN)
s = Solution()
# print(s.levelTraverse(treeN))
s.findPath(treeN,9)
print(s.findPathAns)

