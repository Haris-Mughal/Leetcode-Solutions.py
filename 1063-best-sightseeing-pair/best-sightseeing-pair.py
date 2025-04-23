class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        # n = len(values)

        # first = values[0]
        # max_pair_sum = 0

        # for j in range(1, n):
        #     second = values[j] - j

        #     max_pair_sum = max(max_pair_sum, first + second)
            
        #     first = max(first, values[j] + j)

        # return max_pair_sum
        max_pair_sum = 0
        best_i = values[0] + 0  # values[i] + i

        for j in range(1, len(values)):
            max_pair_sum = max(max_pair_sum, best_i + values[j] - j)
            best_i = max(best_i, values[j] + j)

        return max_pair_sum
