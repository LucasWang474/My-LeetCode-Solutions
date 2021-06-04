# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1. Check if there is a cycle
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        if not (fast and fast.next):
            return None

        # 2. find the joint
        ptr1, ptr2 = head, slow
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next
        return ptr1
