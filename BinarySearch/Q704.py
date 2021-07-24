class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            cmp = target - nums[mid]
            if cmp < 0:
                hi = mid - 1
            elif cmp > 0:
                lo = mid + 1
            else:
                return mid
        return -1
