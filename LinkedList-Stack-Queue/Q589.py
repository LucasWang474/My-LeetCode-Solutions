# https://leetcode.com/prob2lems/n-ary-tree-preorder-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root):
        # Recursive
        if not root:
            return []
        else:
            res = [root.val]
            for child in root.children:
                res.extend(self.preorder(child))
            return res

    def preorder(self, root):
        # Iterative
        res, stack = [], []
        ptr = root
        while ptr or stack:
            if ptr:
                res.append(ptr.val)
                stack.extend(reversed(ptr.children))
                ptr = None
            else:
                ptr = stack.pop()
        return res
