class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

    # Create dictionaries to store character mappings
        map_s_to_t = {}
        map_t_to_s = {}

        for char_s, char_t in zip(s, t):
        # Check if mappings are consistent
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
        
        # Add the mappings
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

        return True