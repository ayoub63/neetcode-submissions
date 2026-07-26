class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , r = 0, len(nums) - 1
        res = nums[0]
        while r > l:
            m = (l + r) // 2
            if nums[r] > nums[l]:
                res = min(res, nums[l])
                break
            if nums[m] >= nums[r]:
               l = m + 1 
               res = min(res, nums[l])

            else: 
               r = m 

        return res

        