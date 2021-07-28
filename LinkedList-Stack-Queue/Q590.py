# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root):
        if not root:
            return []

        # Iterative
        res, stack = [], []
        ptr = root
        while ptr or stack:
            if ptr:
                res.append(ptr.val)
                stack.extend(ptr.children)
                ptr = None
            else:
                ptr = stack.pop()
        return res[::-1]

    def postorder(self, root):
        # Recursive
        if not root:
            return []

        res = []
        for child in root.children:
            res.extend(self.postorder(child))
        res.append(root.val)
        return res
