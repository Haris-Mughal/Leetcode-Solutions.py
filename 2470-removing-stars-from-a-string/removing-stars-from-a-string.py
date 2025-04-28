class Solution:
    def removeStars(self, s: str) -> str:
        
        a = []

        for c in s:
            if c == "*":
                if a: a.pop()

            else:
                a.append(c)
                
        return "".join(a)