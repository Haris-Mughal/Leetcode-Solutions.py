class Solution:
    def checkRecord(self, s: str) -> bool:
        a = 0

        for i in range(len(s)):
            if s[i] == "A":
                a += 1
                
            elif s[i:i+3] == "LLL":
                return False
        
            if a >= 2:
                return False

        return True

