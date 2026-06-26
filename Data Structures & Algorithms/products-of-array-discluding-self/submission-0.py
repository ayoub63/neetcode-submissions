class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        result = []
        product = 1
        while i < len(nums):
            for index , num in enumerate(nums):
                if i != index:
                    product *= num
                    

            result.append(product)
            product = 1
            i += 1

        return result                           