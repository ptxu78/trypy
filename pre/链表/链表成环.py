class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# 快慢指针法
def findbeginofloop(head):
    slow = head  # 慢指针
    fast = head  # 快指针
    if head is None:  # 判断链表是否为空
        return head

    while fast.next != None and fast.next.next != None:  # fastPtr的下一个节点和下下个节点都不为空
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # 两个指针相遇存在环结构
            print("存在环结构")
            break

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2
    findbeginofloop(node1)
