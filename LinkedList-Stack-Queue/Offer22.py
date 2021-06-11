# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
    """

    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        for _ in range(k):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        return slow
