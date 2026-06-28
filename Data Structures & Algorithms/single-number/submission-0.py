class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        duplicates = set()

        for num in nums:
            if num not in duplicates:
                duplicates.add(num)
            
            elif num in duplicates:
                duplicates.remove(num)
               
        return duplicates.pop()