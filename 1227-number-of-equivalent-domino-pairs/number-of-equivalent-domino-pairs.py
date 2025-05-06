class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = [0] * 100  # keys go from 11 to 99
        result = 0

        for a, b in dominoes:
            key = 10 * min(a, b) + max(a, b)
            result += count[key]
            count[key] += 1

        return result
