# https://leetcode.com/problems/maximum-width-of-binary-tree/
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = [(root, 0)]
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)

            new_queue = []
            for node, i in queue:
                if node.left:
                    new_queue.append((node.left, i * 2 + 1))
                if node.right:
                    new_queue.append((node.right, i * 2 + 2))
            queue = new_queue
        return max_width
