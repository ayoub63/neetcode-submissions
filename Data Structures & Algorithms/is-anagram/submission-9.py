class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortierter_string = "".join(sorted(s))
        sortierter_string2 = "".join(sorted(t))

        return sortierter_string == sortierter_string2