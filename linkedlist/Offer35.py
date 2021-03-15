# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        ptr = head
        while ptr:
            next = ptr.next
            ptr.next = Node(ptr.val, next)
            ptr = next

        ptr = head
        while ptr:
            new_next, old_next = ptr.next, ptr.next.next
            new_next.random = ptr.random.next if ptr.random else None
            ptr = old_next

        new_head = head.next
        ptr = head
        while ptr:
            new_next, old_next = ptr.next, ptr.next.next
            new_next.next = old_next.next if old_next else None
            ptr.next = old_next
            ptr = old_next
        return new_head
