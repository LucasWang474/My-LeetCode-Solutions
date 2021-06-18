# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        >>> sol = Solution()
        >>> sol.backspaceCompare("ab#c", "ad#c")
        True
        >>> sol.backspaceCompare("ab##", "c#d#")
        True
        >>> sol.backspaceCompare("a##c", "#a#c")
        True
        >>> sol.backspaceCompare("a#c", "b")
        False
        """

        def to_stack(string: str):
            stack = []
            for c in string:
                if c == "#" and stack:
                    stack.pop()
                else:
                    stack.append(c)
            return stack

        return to_stack(s) == to_stack(t)
