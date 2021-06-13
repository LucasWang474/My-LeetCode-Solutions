# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next

        k %= length
        if k == 0:
            return head

        leftTail = head
        for _ in range(length - k - 1):
            leftTail = leftTail.next

        rightHead = leftTail.next
        leftTail.next = None
        tail.next = head
        return rightHead
