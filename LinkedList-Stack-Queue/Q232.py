# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_out = []
        self.stack_in = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_out.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        return self.stack_in.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack_in:
            while self.stack_out:
                self.stack_in.append(self.stack_out.pop())
        return self.stack_in[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack_out and not self.stack_in

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
