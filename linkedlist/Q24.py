# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        ptr = dummy = ListNode(0, head)
        while ptr.next and ptr.next.next:
            first = ptr.next
            second = first.next

            first.next = second.next
            second.next = first
            ptr.next = second
            ptr = first
        return dummy.next
