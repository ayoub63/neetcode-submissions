class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        
            

        for i in range(len(nums)):
            mid = (left + right) // 2
            if nums[i] == target:
                return i

            elif target > nums[mid]:
                left += 1

            else:
                right -= 1

        return -1