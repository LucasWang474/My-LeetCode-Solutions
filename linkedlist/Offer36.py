# Definition for a Node.
from typing import Tuple


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        head, tail = self.flatten(root)
        head.left = tail
        tail.right = head
        return head

    def flatten(self, root: 'Node'):
        """ 
        Accept root, return head and tail of the flattened tree
        """
        if not root:
            return None, None

        head = tail = root
        if root.left:
            head, left_tail = self.flatten(root.left)
            root.left, left_tail.right = left_tail, root

        if root.right:
            right_head, tail = self.flatten(root.right)
            root.right, right_head.left = right_head, root

        return head, tail

sample = Node(4, Node(2, Node(1), Node(3)), Node(5))
result = Solution().treeToDoublyList(sample)
print(result)