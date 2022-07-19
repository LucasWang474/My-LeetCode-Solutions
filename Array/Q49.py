# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - 97] += 1
            key = tuple(counts)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]
        return list(res.values())
