class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head:ListNode):
    while head:
        print(head.val, ' -> ',end='')
        head = head.next
    print()
def reverseRec(pre,cur):
    if not cur:
        return pre
    nxt = cur.next
    cur.next = pre
    return reverseRec(cur,nxt)

lastNode = None
lenList = 10
for i in range(lenList,0,-1):
    newNode = ListNode(i)
    newNode.next = lastNode
    lastNode = newNode
head = lastNode

def reverseNotRec(headNode):
    head = headNode
    cur = tail = head
    cur = cur.next
    nxt = cur.next
    for i in range(lenList-1):
        cur.next = head
        tail.next = nxt
        head = cur
        cur = nxt
        if cur:
            nxt = cur.next
        # printList(head)
    return head
def reverseNotRec2(headNode,preNum,aftNum):
    pre = headNode
    for i in range(preNum-2):
        pre = pre.next
    aft = headNode
    for i in range(aftNum):
        aft = aft.next
    tail = pre.next
    cur = tail.next
    nxt = cur.next

    for i in range(aftNum-preNum):
        cur.next = pre.next
        tail.next = nxt
        pre.next = cur
        cur = nxt
        if cur:
            nxt = cur.next
        printList(headNode)



printList(lastNode)

# i = reverseRec(None, head)
# i = reverseNotRec(head)
def 逆序打印(cur):
    if not cur:
        return
    else:
        逆序打印(cur.next)
        print(cur.val)
逆序打印(head)