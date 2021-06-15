# https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.deque = [-1] * k
        self.size = 0
        self.head = 0
        self.tail = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """

        if self.isFull():
            return False

        if not self.isEmpty():
            self.head = (self.head - 1) % len(self.deque)
        self.deque[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if not self.isEmpty():
            self.tail = (self.tail + 1) % len(self.deque)
        self.deque[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % len(self.deque)
        self.size -= 1
        if self.size <= 0:
            self.head = 0
            self.tail = 0
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.tail = (self.tail - 1) % len(self.deque)
        self.size -= 1
        if self.size <= 0:
            self.head = 0
            self.tail = 0
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.deque[self.head] if not self.isEmpty() else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.deque[self.tail] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size <= 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == len(self.deque)

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront",
    "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
