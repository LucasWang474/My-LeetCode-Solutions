# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        return " ".join(map(lambda word: word[:-1], sorted(s.split(" "), key=lambda word: word[-1])))
