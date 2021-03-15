# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/
    """

    def reverseList(self, head: ListNode) -> ListNode:
        reversed = None
        while head:
            temp = head.next
            head.next = reversed
            reversed = head
            head = temp
        return reversed