# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # recursive
        self.flatten_helper(root)
        return root

    def flatten_helper(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        leftRoot = root.left
        leftTail = self.flatten_helper(root.left)
        rightRoot = root.right
        rightTail = self.flatten_helper(root.right)

        if leftRoot:
            root.left = None
            root.right = leftRoot
            root = leftTail
        if rightRoot:
            root.right = rightRoot
            root = rightTail
        return root

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # iterative
        cur = root
        while cur:
            if cur.left:
                rightmost = cur.left
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
