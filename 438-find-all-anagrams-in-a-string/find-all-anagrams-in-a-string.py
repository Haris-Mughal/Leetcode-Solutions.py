class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        hash_p = Counter(p)    
        l, window, ans = 0, {}, []

        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 1

            else:
                window[s[r]] += 1

            if (r - l + 1) < len(p):
                continue

            elif (r - l + 1) == len(p):
                if window == hash_p:
                    ans.append(l)
                    
            else:
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]
                l+=1

                if window == hash_p:
                    ans.append(l)

        return ans