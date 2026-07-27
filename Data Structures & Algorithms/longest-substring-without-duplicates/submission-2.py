class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       n = len(s)
       l = 0
       du = set() 
       ans = 0
       for r in range(n):
           while s[r] in du:
                du.remove(s[l])
                l+= 1


           ans = max((r - l) + 1, ans)
           du.add(s[r])

       return ans  
