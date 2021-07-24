# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums):
        self.mergeSort(nums)
        return nums

    def mergeSort(self, nums):
        if len(nums) < 2:
            return

        mid = len(nums) // 2
        left, right = nums[:mid], nums[mid:]
        self.mergeSort(left)
        self.mergeSort(right)

        i = j = k = 0
        while i < len(left) or j < len(right):
            if j >= len(right) or i < len(left) and left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
