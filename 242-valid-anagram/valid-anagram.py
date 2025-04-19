class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return sorted(s) == sorted(t)

        # ---
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t

        # ---
        # if len(s) != len(t):
        #     return False

        # stack = list(s)
        # queue = deque(t)

        # count_s = {}
        # count_t = {}

        # while stack:
        #     ch = stack.pop()
        #     count_s[ch] = count_s.get(ch, 0) + 1

        # while queue:
        #     ch = queue.popleft()
        #     count_t[ch] = count_t.get(ch, 0) + 1

        # return count_s == count_t
