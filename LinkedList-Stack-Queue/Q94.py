# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, res = [], []
        ptr = root
        while stack or ptr:
            while ptr:
                stack.append(ptr)
                ptr = ptr.left

            ptr = stack.pop()
            res.append(ptr.val)
            ptr = ptr.right
        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # Morris Traversal
        res = []
        ptr = root
        while ptr:
            if not ptr.left:
                res.append(ptr.val)
                ptr = ptr.right
            else:
                right_most = ptr.left
                while right_most.right:
                    right_most = right_most.right

                left_root = ptr.left
                right_most.right = ptr
                ptr.left = None
                ptr = left_root
        return res
