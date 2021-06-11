# https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        toNextGreater = dict()
        prevs = []
        for num in nums2:
            while prevs and num > prevs[-1]:
                toNextGreater[prevs.pop()] = num
            prevs.append(num)

        return [toNextGreater.get(num, -1) for num in nums1]
