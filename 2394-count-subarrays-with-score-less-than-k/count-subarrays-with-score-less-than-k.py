class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        left = 0
        sum_window = 0
        window = 0
        answer = 0

        for right in range(len(nums)):
            window = (right - left) + 1
            sum_window += nums[right]

            while window * sum_window >= k:
                sum_window -= nums[left]
                left += 1
                window -= 1

            if window * sum_window < k:
                answer += window
                
        return answer

