# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        ptr = head
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next

        N = len(vals)
        for i in range(N // 2):
            if vals[i] != vals[N - i - 1]:
                return False
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        # O(1) space

        # 1. find the rightHead
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        rightHead = slow.next if fast else slow

        # 2. reverse the right part
        reversed = None
        while rightHead:
            next = rightHead.next
            rightHead.next = reversed
            reversed = rightHead
            rightHead = next

        # 3. check one by one
        while reversed:
            if reversed.val != head.val:
                return False
            reversed, head = reversed.next, head.next
        return True
