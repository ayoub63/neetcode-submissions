class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        du = set()

        for n in nums:
            if n not in du:
                du.add(n)

            else:
                return True
        
        return False