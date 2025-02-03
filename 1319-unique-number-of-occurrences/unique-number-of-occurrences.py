class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # freq = {1:3, 2:2, 3:1}

        occur = set()

        for i in freq.values():

            if i in occur:
                return False

            occur.add(i)

        return True

