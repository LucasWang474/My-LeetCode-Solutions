# https://leetcode.com/problems/number-of-recent-calls/

from collections import deque


class RecentCounter:
    def __init__(self):
        self.times = deque()
        self.interval = 3000  # milliseconds

    def ping(self, time: int) -> int:
        self.times.append(time)
        while (self.times[-1] - self.times[0]) > self.interval:
            self.times.popleft()
        return len(self.times)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
