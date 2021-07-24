# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # No extra space
        i, j = m - 1, n - 1
        for k in reversed(range(m + n)):
            if j < 0 or i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # O(n) space
        temp = nums1[:m] + nums2

        i, j = 0, m
        for k in range(m + n):
            if j >= m + n or i < m and temp[i] <= temp[j]:
                nums1[k] = temp[i]
                i += 1
            else:
                nums1[k] = temp[j]
                j += 1
