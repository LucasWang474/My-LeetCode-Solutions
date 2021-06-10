# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None

        ptr = dummy = ListNode(head.val - 1, head)
        prevVal = ptr.val
        while ptr.next:
            if ptr.next.val == prevVal:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
                prevVal = ptr.val
        return dummy.next
