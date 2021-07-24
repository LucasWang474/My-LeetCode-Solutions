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
        ptr = head
        while ptr:
            if not ptr.child:
                ptr = ptr.next
            else:
                child_tail = ptr.child
                while child_tail.next:
                    child_tail = child_tail.next

                if ptr.next:
                    child_tail.next = ptr.next
                    ptr.next.prev = child_tail

                ptr.next = ptr.child
                ptr.next.prev = ptr
                ptr.child = None
        return head
