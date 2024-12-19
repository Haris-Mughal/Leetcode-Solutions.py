class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        no = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[no], nums[i] = nums[i], nums[no]
                no += 1      