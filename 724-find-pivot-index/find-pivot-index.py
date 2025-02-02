class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            
            if 2 * leftSum + nums[i] == total:
                return i

            leftSum += nums[i]

        return -1