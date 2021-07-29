class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num_to_i = dict()
        for i, num in enumerate(sorted(nums)):
            num_to_i.setdefault(num, i)
        return [num_to_i[num] for num in nums]
