class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(map(lambda ele: ele ** 2, nums))

    def sortedSquares(self, nums: List[int]) -> List[int]:
        non_negative_start = 0
        while non_negative_start < len(nums) and nums[non_negative_start] < 0:
            nums[non_negative_start] **= 2
            non_negative_start += 1

        left = list(reversed(nums[:non_negative_start]))
        i, j = 0, non_negative_start
        for k in range(len(nums)):
            if j >= len(nums) or i < len(left) and nums[i] < nums[j]:
                nums[k] = left[i]
                i += 1
            elif i < len(left):
                nums[k] = nums[j]
                j += 1
            else:
                break
        return nums
