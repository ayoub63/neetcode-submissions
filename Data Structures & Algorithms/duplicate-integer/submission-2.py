class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_el = set()
        for num in nums:
            if num  in unique_el:
                return True
            
            unique_el.add(num)
        
        return False
        
