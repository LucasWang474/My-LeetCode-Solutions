# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/sort-array-by-parity-ii/discuss/205903/Python-one-pass-O(1)-memory-simple-code-beats-90
        even, odd, N = 0, 1, len(nums)
        while even < N and odd < N:
            if nums[even] % 2 == 0:
                even += 2
            elif nums[odd] % 2 == 1:
                odd += 2
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
        return nums
