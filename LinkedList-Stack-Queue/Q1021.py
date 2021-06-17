# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        """
        >>> Solution().removeOuterParentheses("(()())(())(()(()))")
        '()()()()(())'
        """
        stack, res = [], []
        depth = 0
        for c in s:
            stack.append(c)
            depth += 1 if c == '(' else -1

            if depth == 0 and stack:
                res += stack[1:-1]
                stack = []
        return "".join(res)

    def removeOuterParentheses(self, s: str) -> str:
        res, opened = [], 0
        for c in s:
            if c == '(' and opened > 0:
                res.append(c)
            if c == ')' and opened > 1:
                res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)
