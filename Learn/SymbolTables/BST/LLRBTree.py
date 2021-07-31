class Node:
    RED = True

    def __init__(self, key, val, color=RED, left=None, right=None):
        self.key = key
        self.val = val
        self.color = color
        self.left = left
        self.right = right

    @staticmethod
    def is_red(node):
        return node and node.color == Node.RED
