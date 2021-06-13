# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

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

        while ptr.next and ptr.next.next:
            if ptr.next.val == ptr.next.next.val:
                duplicate = ptr.next.val
                while ptr.next and ptr.next.val == duplicate:
                    ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return dummy.next
