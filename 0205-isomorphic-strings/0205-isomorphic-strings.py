class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        # Track unique characters and assign them IDs
        char_to_id = {}
        next_id = 0
        s_pattern = []
        t_pattern = []
        
        # Build pattern for string s
        for char in s:
            if char not in char_to_id:
                char_to_id[char] = next_id
                next_id += 1
            s_pattern.append(char_to_id[char])
        
        # Reset for string t (important!)
        char_to_id = {}
        next_id = 0
        
        # Build pattern for string t
        for char in t:
            if char not in char_to_id:
                char_to_id[char] = next_id
                next_id += 1
            t_pattern.append(char_to_id[char])
        
        # Compare patterns
        return s_pattern == t_pattern