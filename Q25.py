# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ptr = dummy = ListNode(0, head)
        while ptr.next:
            oldHead = ptr.next

            oldTail = ptr
            for _ in range(k):
                if not oldTail:
                    break
                oldTail = oldTail.next
            if not oldTail:
                break

            next = oldTail.next
            oldTail.next = None

            newHead = self.reverseList(oldHead)
            oldHead.next = next
            ptr.next = newHead
            ptr = oldHead

        return dummy.next

    def reverseList(self, head):
        res = None
        while head:
            next = head.next
            head.next = res
            res = head
            head = next
        return res
