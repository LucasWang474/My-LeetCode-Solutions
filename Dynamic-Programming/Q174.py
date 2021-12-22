# https://leetcode.com/problems/dungeon-game/
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        hp = [row + [float('inf')] for row in dungeon]
        hp.append([float('inf')] * (N + 1))
        hp[M][N - 1] = 1
        hp[M - 1][N] = 1

        for r in reversed(range(M)):
            for c in reversed(range(N)):
                hp[r][c] = max(1, min(hp[r][c + 1], hp[r + 1][c]) - dungeon[r][c])

        return hp[0][0]
