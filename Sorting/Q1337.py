# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sorted_indices = sorted(range(len(mat)), key=lambda i: sum(mat[i]))
        return sorted_indices[:k]
