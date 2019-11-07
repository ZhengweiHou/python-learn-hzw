'''merge-two-sorted-lists'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tempNode1,tempNode2 = l1,l2
        return_Node=ListNode(99)
        temp=return_Node

        while tempNode2 is not None and tempNode1 is not None:
            if tempNode1.val > tempNode2.val:
                temp.next=tempNode2
                tempNode2 = tempNode2.next
            else:
                temp.next = tempNode1
                tempNode1 = tempNode1.next
            temp = temp.next

        if tempNode1 is not None:
            temp.next = tempNode1
        if tempNode2 is not None:
            temp.next = tempNode2

        return return_Node.next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2

