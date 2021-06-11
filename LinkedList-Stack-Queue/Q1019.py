# https://leetcode.com/problems/next-greater-node-in-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode):
        # Brute force
        result = []
        while head:
            result.append(0)

            next = head.next
            while next:
                if next.val > head.val:
                    result[-1] = next.val
                    break
                next = next.next
            head = head.next
        return result

    def nextLargerNodes(self, head: ListNode) -> list:
        # Stack
        vals = []
        ptr = head
        while ptr:
            vals.append(ptr.val)
            ptr = ptr.next

        stack, res = [], [0] * len(vals)
        for i in range(len(vals)):
            while stack and vals[stack[-1]] < vals[i]:
                res[stack.pop()] = vals[i]
            stack.append(i)

        return res

    def nextLargerNodes(self, head: ListNode) -> list:
        # Stack 2
        stack, res = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append([len(res), head.val])
            res.append(0)
            head = head.next
        return res
