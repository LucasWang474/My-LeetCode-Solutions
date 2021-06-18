# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        """
        >>> sol = Solution()
        >>> sol.makeGood("leEeetcode")
        'leetcode'
        >>> sol.makeGood("abBAcC")
        ''
        >>> sol.makeGood("s")
        's'
        """
        stack = []
        for c in s:
            if stack and stack[-1].lower() == c.lower() and stack[-1] != c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
