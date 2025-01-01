class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        curr = 0
        maxa = 0

        for g in gain:
            curr +=g
            maxa = max(maxa, curr)

        return maxa