# https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ptrLess = less = ListNode()
        ptrOther = other = ListNode()

        while head:
            if head.val < x:
                ptrLess.next = head
                ptrLess = ptrLess.next
            else:
                ptrOther.next = head
                ptrOther = ptrOther.next
            head = head.next

        if ptrLess:
            ptrLess.next = other.next
            if ptrOther:
                ptrOther.next = None
            return less.next
        else:
            return other.next
