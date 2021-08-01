class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        dif = sorted_arr[0] - sorted_arr[1]
        return all(x - y == dif for x, y in zip(sorted_arr[1:], sorted_arr[2:]))

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_num, max_num = min(arr), max(arr)
        step = (max_num - min_num) / (len(arr) - 1)

        if step == 0:
            return True

        diffs = set(num - min_num for num in arr)
        return len(diffs) == len(arr) and all(diff % step == 0 for diff in diffs)
