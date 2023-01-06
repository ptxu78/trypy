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
T = cons()

def DFS(rootNode):
    if not rootNode:
        return
    else:
        DFS(rootNode.left)
        print(rootNode.val)
        DFS(rootNode.right)
def 中序遍历非递归(rootNode):
    supStack = []
    tree = rootNode
    while supStack or tree:
        if tree:
            supStack.append(tree)
            tree = tree.left
        else:
            tree = supStack.pop()
            print(tree.val)
            tree = tree.right
中序遍历非递归(T)
