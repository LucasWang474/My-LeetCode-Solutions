# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num_to_i = {num: i for i, num in enumerate(arr2)}
        max_num = max(arr1)
        arr1.sort(key=lambda x: num_to_i[x] if x in num_to_i else x + max_num)
        return arr1
