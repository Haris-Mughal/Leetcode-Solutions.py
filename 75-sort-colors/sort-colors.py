class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums) -1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        while i <= r:
            
            if nums[i] == 0:
                swap(i, l)
                i += 1
                l += 1

            elif nums[i] == 2:
                swap(i, r)
                r -= 1

            else:
                i += 1