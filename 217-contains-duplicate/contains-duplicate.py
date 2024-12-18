class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()

        for n in nums:
            if n in result:
                return True
            
            result.add(n)
        
        return False