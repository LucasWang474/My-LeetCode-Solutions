# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode):
        result = []
        while head:
            result.append(0)

            next = head.next
            while next:
                if next.val > head.val:
                    result[-1] = next.val
                    break
                next = next.next
            head = head.next
        return result
