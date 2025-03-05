class Solution:
    def coloredCells(self, n: int) -> int:

        x = n
        y = x * 2 - 2

        return x * y + 1