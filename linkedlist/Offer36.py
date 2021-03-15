# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def dfs(cur_root: 'Node'):
            if not cur_root:
                return None

            dfs(cur_root.left)

            if self.tail:
                self.tail.right, cur_root.left = cur_root, self.tail
            else:
                self.head = cur_root
            self.tail = cur_root

            dfs(cur_root.right)

        if not root:
            return None

        self.head = self.tail = None
        dfs(root)
        self.head.left, self.tail.right = self.tail, self.head
        return self.head


class Solution1:
    # https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        head, tail = self.flatten(root)
        head.left, tail.right = tail, head
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
result = Solution1().treeToDoublyList(sample)
print(result)
