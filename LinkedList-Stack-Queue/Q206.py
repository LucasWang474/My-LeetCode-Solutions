# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative
        reversed = None
        while head:
            next = head.next
            head.next = reversed
            reversed = head
            head = next
        return reversed

    def reverseList(self, head: ListNode) -> ListNode:
        # Recursive
        if not head or not head.next:
            return head

        newTail = head.next
        newHead = self.reverseList(head.next)
        newTail.next = head
        head.next = None
        return newHead
