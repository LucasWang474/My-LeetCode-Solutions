# https://leetcode.com/problems/copy-list-with-random-pointer/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        ptr = head
        while ptr:
            ptr.next = Node(ptr.val, ptr.next)
            ptr = ptr.next.next

        ptr = head
        while ptr:
            if ptr.random:
                ptr.next.random = ptr.random.next
            ptr = ptr.next.next

        new_head = head.next
        ptr = head
        while ptr:
            old_next = ptr.next.next
            new_next = ptr.next

            new_next.next = old_next.next if old_next else None
            ptr.next = old_next
            ptr = ptr.next
        return new_head
