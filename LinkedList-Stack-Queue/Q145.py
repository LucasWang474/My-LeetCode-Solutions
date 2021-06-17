# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursive
        res = []
        self.recur_helper(root, res)
        return res

    def recur_helper(self, root, res):
        if not root:
            return

        self.recur_helper(root.left, res)
        self.recur_helper(root.right, res)
        res.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative
        stack, res = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        while root or stack:
            while root:
                stack.append(root.val)
                stack.append(root.right)
                root = root.left

            while stack and isinstance(stack[-1], int):
                res.append(stack.pop())

            if stack:
                root = stack.pop()
        return res
