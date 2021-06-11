# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        left = head
        for _ in range(k - 1):
            left = left.next

        slow, fast = head, left.next
        while fast:
            slow, fast = slow.next, fast.next

        right = slow
        left.val, right.val = right.val, left.val
        return head
