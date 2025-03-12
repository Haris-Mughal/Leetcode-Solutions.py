class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        res = []
        
        for w1, w2 in zip(word1, word2):
            res.append(w1)
            res.append(w2)

        res.append(word1[len(word2):])
        res.append(word2[len(word1):])

        return "".join(res)