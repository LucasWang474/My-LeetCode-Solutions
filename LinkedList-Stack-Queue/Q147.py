# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        vals = []
        ptr = head
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next

        for i in range(len(vals)):
            for j in reversed(range(1, i + 1)):
                if vals[j] < vals[j - 1]:
                    vals[j], vals[j - 1] = vals[j - 1], vals[j]
                else:
                    break

        ptr = dummy = ListNode()
        for val in vals:
            ptr.next = ListNode(val)
            ptr = ptr.next
        return dummy.next
