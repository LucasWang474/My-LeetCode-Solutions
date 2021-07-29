# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = 0, len(nums) - 1
        while even < odd:
            if nums[even] % 2 == 0:
                even += 1
            else:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd -= 1
        return nums
