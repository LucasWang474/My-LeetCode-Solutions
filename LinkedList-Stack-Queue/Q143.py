# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        slow = fast = ListNode(0, head)
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid = slow
        right = mid.next
        mid.next = None

        reversed = None
        while right:
            next = right.next
            right.next = reversed
            reversed = right
            right = next
        right = reversed

        left = head
        while right:
            nextLeft = left.next

            left.next = right
            right = right.next
            left.next.next = nextLeft
            left = nextLeft
        return head
