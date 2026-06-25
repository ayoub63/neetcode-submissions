class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_str = {}
        t_str = {}
        if len(s) != len(t):
            return False

        for c1, c2 in zip(s, t):
            if c1 in s_str:
                s_str[c1] += 1
            else:
                s_str[c1] = 1
            if c2 in t_str:
                t_str[c2] += 1 
            else:  
                t_str[c2] = 1

        return s_str == t_str