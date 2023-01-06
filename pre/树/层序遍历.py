class treeNode:
    def __init__(self,val = -1, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
consList = [1,2,3,4,9,5,6,7,8]

def cons(ptr = 0):
    if ptr < len(consList) and consList[ptr] != 'N':
        newNode = treeNode(consList[ptr])
        newNode.left = cons(2*ptr + 1)
        newNode.right = cons(2*ptr + 2)
        return newNode
    else:
        return None

def cengxubianli(root):
    supQueue = []
    supQueue.append(root)
    while(supQueue):
        temList = supQueue.copy()
        supQueue = []
        while temList:
            curNode = temList.pop(0)
            if curNode.left:
                supQueue.append(curNode.left)
            if curNode.right:
                supQueue.append(curNode.right)
            print(curNode.val, end = ' ')
        print()

T = cons()
cengxubianli(T)