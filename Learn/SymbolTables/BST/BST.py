class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def get(self, key):
        ptr = self.root
        while ptr:
            if key < ptr.key:
                ptr = ptr.left
            elif key > ptr.key:
                ptr = ptr.right
            else:
                return ptr.val
        return None

    def put(self, key, val):
        self.root = self.put_helper(self.root, key, val)

    def put_helper(self, cur, key, val):
        if not cur:
            return Node(key, val)

        if key < cur.key:
            cur.left = self.put_helper(cur.left, key, val)
        elif key > cur.key:
            cur.right = self.put_helper(cur.right, key, val)
        else:
            cur.val = val

        return cur

    def min(self):
        ptr = self.root
        while ptr:
            if not ptr.left:
                return ptr.key
            else:
                ptr = ptr.left

    def max(self):
        ptr = self.root
        while ptr:
            if not ptr.right:
                return ptr.key
            else:
                ptr = ptr.right

    def floor(self, key):
        ptr = self.root
        res = None
        while ptr:
            if ptr.key < key:
                res = ptr.key
                ptr = ptr.right
            elif ptr.key > key:
                ptr = ptr.left
            else:
                return ptr.key
        return res

    def ceil(self, key):
        ptr = self.root
        res = None
        while ptr:
            if ptr.key < key:
                ptr = ptr.right
            elif ptr.key > key:
                res = ptr.key
                ptr = ptr.left
            else:
                return ptr.key
        return res
