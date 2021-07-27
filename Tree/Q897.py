# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        new_root = None
        prev, cur = None, root
        while cur:
            if not cur.left:
                if not new_root:
                    new_root = cur
                prev, cur = cur, cur.right
            else:
                right_most = cur.left
                while right_most.right:
                    right_most = right_most.right

                next_cur = cur.left
                cur.left = None
                right_most.right = cur
                if prev:
                    prev.right = next_cur
                cur = next_cur
        return new_root
