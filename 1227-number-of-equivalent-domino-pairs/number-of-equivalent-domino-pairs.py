class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        result = 0

        for a, b in dominoes:
            key = (min(a, b), max(a, b))
        
            if key in count:
                result += count[key]
                count[key] += 1
            else:
                count[key] = 1

        return result
        
