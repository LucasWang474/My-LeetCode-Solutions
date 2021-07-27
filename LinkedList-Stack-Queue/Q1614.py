# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = cur_depth = 0
        for c in s:
            if c == '(':
                cur_depth += 1
            elif c == ')':
                cur_depth -= 1

            if cur_depth > max_depth:
                max_depth = cur_depth
        return max_depth
