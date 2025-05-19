class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:

        base = minutesToTest // minutesToDie + 1
        pigs = 0
        x = 1

        while x < buckets:
            pigs += 1
            x *= base

        return pigs