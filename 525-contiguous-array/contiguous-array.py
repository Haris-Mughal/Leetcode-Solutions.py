class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {}

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        res = 0
        sum_ = 0

        for i in range(len(nums)):
            sum_ += nums[i]

            if sum_ == 0:
                res = max(res, i + 1)

            if sum_ in mp:
                res = max(res, i - mp[sum_])
            else:
                mp[sum_] = i

        return res