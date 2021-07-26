# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
import collections


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = collections.Counter(students)
        i = 0
        while i < len(students) and count[sandwiches[i]] > 0:
            count[sandwiches[i]] -= 1
            i += 1
        return len(students) - i
