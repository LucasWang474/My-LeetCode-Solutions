# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative
        stack, res = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root.right)
                root = root.left

            root = stack.pop()
        return res
