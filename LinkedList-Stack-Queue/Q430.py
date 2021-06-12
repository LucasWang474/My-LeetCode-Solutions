# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Recursive
        self.flatten_helper(head)
        return head

    def flatten_helper(self, head):
        if not head:
            return None
        if not head.child:
            if not head.next:
                return head
            else:
                return self.flatten_helper(head.next)

        childRoot = head.child
        childTail = self.flatten_helper(childRoot)

        oldNext = head.next
        head.next = childRoot
        childRoot.prev = head
        head.child = None

        childTail.next = oldNext
        if oldNext:
            oldNext.prev = childTail
            return self.flatten_helper(oldNext)
        else:
            return childTail
