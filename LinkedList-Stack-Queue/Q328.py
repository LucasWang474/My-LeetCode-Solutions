# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        oddHead, evenHead = head, head.next

        oddPtr, evenPtr = oddHead, evenHead
        while evenPtr and evenPtr.next:
            nextOdd = evenPtr.next

            oddPtr.next = nextOdd
            oddPtr = oddPtr.next

            evenPtr.next = nextOdd.next
            evenPtr = evenPtr.next

        oddPtr.next = evenHead
        return oddHead
