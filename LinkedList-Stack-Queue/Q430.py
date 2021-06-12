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

        childHead = head.child
        childTail = self.flatten_helper(childHead)

        oldNext = head.next
        head.next = childHead
        childHead.prev = head
        head.child = None

        childTail.next = oldNext
        if oldNext:
            oldNext.prev = childTail
            return self.flatten_helper(oldNext)
        else:
            return childTail

    def flatten(self, head: 'Node') -> 'Node':
        # Iterative
        if not head:
            return None

        ptr = head
        while ptr:
            if not ptr.child:
                ptr = ptr.next
                continue

            childHead = ptr.child
            childTail = ptr.child
            while childTail.next:
                childTail = childTail.next

            oldNext = ptr.next
            ptr.next = childHead
            childHead.prev = ptr
            ptr.child = None

            if oldNext:
                childTail.next = oldNext
                oldNext.prev = childTail

            ptr = ptr.next
        return head
