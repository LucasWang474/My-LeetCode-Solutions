# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()

        res = []
        res_total, nums_total = 0, sum(nums)
        while res_total <= nums_total:
            cur = nums.pop()
            res.append(cur)
            res_total += cur
            nums_total -= cur
        return res
