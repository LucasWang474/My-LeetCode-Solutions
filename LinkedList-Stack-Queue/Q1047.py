class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        >>> Solution().removeDuplicates("abbaca")
        'ca'
        >>> Solution().removeDuplicates("azxxzy")
        'ay'Q

        """
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
