'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:

    def __addwoNumbers(self, l1: ListNode, l2: ListNode, flag: bool) -> ListNode:
        if l1 is None and l2 is None:
            if flag:
                return ListNode(int(flag))
            else:
                return None
        else:
            # v1 = 0 if l1 is None else l1.val
            # v2 = 0 if l2 is None else l2.val
            v = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + flag
            temp = ListNode(v%10)
            temp.next = self.__addwoNumbers(
                None if l1 is None else l1.next,
                None if l2 is None else l2.next,
                v>=10)
            return temp



    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.__addwoNumbers(l1,l2,False)


def showListNode(l: ListNode):
    if l is not None:
        print(l.val,end=' ')
        showListNode(l.next)
    else:
        print()


sl = Solution1()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
showListNode(sl.addTwoNumbers(l1,l2))


l1 = ListNode(1)
l2 = ListNode(9)
l2.next = ListNode(9)
showListNode(sl.addTwoNumbers(l1,l2))

