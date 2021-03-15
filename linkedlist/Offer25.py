# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """ 
    https://leetcode-cn.com/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ptr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next
        ptr.next = l1 if l1 else l2
        return dummy.next