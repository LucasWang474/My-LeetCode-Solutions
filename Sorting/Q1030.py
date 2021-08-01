# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = [(x, y) for x in range(rows) for y in range(cols)]
        res.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))
        return res
