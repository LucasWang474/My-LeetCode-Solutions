# https://leetcode.com/problems/maximum-units-on-a-truck/

class Solution:
    def maximumUnits(self, box_types: List[List[int]], truck_size: int) -> int:
        total_units = 0
        for box_type in sorted(box_types, key=lambda ele: ele[1], reverse=True):
            if truck_size <= 0:
                break

            num = min(truck_size, box_type[0])
            total_units += box_type[1] * num
            truck_size -= num
        return total_units
