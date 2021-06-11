# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        left = list1
        for _ in range(a - 1):
            left = left.next

        right = left
        for _ in range(b - a + 1):
            right = right.next

        left.next = list2
        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = right.next
        return list1
