from typing import List

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def check(val):
            rotations_top = rotations_bottom = 0
            for i in range(len(tops)):
                if tops[i] != val and bottoms[i] != val:
                    return float('inf')  # Not possible
                elif tops[i] != val:
                    rotations_top += 1
                elif bottoms[i] != val:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        result = min(check(tops[0]), check(bottoms[0]))
        return result if result != float('inf') else -1
