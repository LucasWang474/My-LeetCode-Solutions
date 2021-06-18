# https://leetcode.com/problems/backspace-string-compare/
import itertools


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

        def helper(string: str):
            skip = 0
            for c in reversed(string):
                if c == "#":
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield c

        return all(x == y for x, y in itertools.zip_longest(helper(s), helper(t)))
