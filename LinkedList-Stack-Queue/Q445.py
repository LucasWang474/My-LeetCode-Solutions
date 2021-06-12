# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def pushAllToStack(root):
            stack = []
            while root:
                stack.append(root.val)
                root = root.next
            return stack

        stack1, stack2 = pushAllToStack(l1), pushAllToStack(l2)

        carry = 0
        res = None
        while stack1 or stack2 or carry > 0:
            total = carry
            if stack1:
                total += stack1.pop()
            if stack2:
                total += stack2.pop()
            carry = total // 10
            cur = ListNode(total % 10)
            cur.next = res
            res = cur
        return res

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toInt(root):
            res = 0
            while root:
                res = res * 10 + root.val
                root = root.next
            return res

        total = toInt(l1) + toInt(l2)
        res = None
        while total > 0:
            cur = ListNode(total % 10)
            cur.next = res
            res = cur
            total //= 10
        return res if res else ListNode(0)
