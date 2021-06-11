# https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums):
        N = len(nums)
        res, stack = [-1] * N, []

        for i in range(N * 2):
            i %= N
            cur = nums[i]
            while stack and nums[stack[-1]] < cur:
                res[stack.pop()] = cur
            stack.append(i)

        return res
