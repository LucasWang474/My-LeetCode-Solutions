from functools import cache


# https://leetcode.com/problems/burst-balloons/
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1, *nums, 1]

        @cache
        def dp(L, R):
            if L > R:
                return 0

            return max(
                dp(L, i - 1) + nums[L - 1] * nums[i] * nums[R + 1] + dp(i + 1, R)
                for i in range(L, R + 1)
            )

        return dp(1, len(nums) - 2)
