class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l, s, w, ans = 0, 0, 0, 0

        for r in range(len(nums)):
            w=(r-l)+1
            s+=nums[r]

            while w*s>=k:
                s-=nums[l]
                l+=1
                w-=1

            if w*s<k:
                ans+=w
        return ans

