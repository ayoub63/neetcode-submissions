class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        duplicates = set()
        count = 0
        for r in range(len(s)):
            while s[r] in duplicates:
                duplicates.remove(s[l]) 
                l += 1 
                  
                   

                
            duplicates.add(s[r])
            count = max(count, (r - l) + 1)
            

        return count

        

