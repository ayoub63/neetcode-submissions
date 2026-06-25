class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_table = {}
        s_table = {}

        for char in s:
            s_table[char] = s_table.get(char, 0) + 1 

        
        for char in t:
            t_table[char] = t_table.get(char, 0) + 1     

        
        return t_table == s_table