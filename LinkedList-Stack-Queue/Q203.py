# https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None

        ptr = dummy = ListNode(val - 1, head)

        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
