class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0
        duplicates = set()
        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l])
                l += 1

            count = max((r-l) + 1, count)
            duplicates.add(s[r])

        return count

            
