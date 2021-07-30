# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
import collections


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # return target == sorted(arr)
        return collections.Counter(target) == collections.Counter(arr)
