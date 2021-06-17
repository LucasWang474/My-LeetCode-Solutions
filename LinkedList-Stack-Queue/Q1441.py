# https://leetcode.com/problems/build-an-array-with-stack-operations

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        i = 0
        for cur in range(1, n + 1):
            if i == len(target):
                break

            res.append("Push")
            if cur == target[i]:
                i += 1
            elif cur < target[i]:
                res.append("Pop")
        return res
