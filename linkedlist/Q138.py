# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # Use hash table, two pass

        if not head:
            return None

        oldToNew = dict()

        # 1. shadow copy
        ptr = head
        while ptr:
            oldToNew[ptr] = Node(ptr.val, ptr.next, ptr.random)
            ptr = ptr.next

        # 2. repace next and random
        ptr = head
        while ptr:
            if ptr.next:
                oldToNew[ptr].next = oldToNew[oldToNew[ptr].next]
            if ptr.random:
                oldToNew[ptr].random = oldToNew[oldToNew[ptr].random]
            ptr = ptr.next

        return oldToNew[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        # No extra space, no hash table

        if not head:
            return None

        # 1. shadow copy
        ptr = head
        while ptr:
            oldNext = ptr.next
            copy = Node(ptr.val, oldNext)
            ptr.next = copy
            ptr = oldNext

        # 2. copy actual random pointer
        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        # 3. restore original list and construct new list
        newHead = head.next
        ptr = head
        while ptr:
            oldNext = ptr.next.next
            newNext = ptr.next
            newNext.next = oldNext.next if oldNext else None
            ptr.next = oldNext
            ptr = oldNext
        return newHead
