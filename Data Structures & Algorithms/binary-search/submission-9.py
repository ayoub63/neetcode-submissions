class Solution:
    def search(self, nums: List[int], target: int) -> int:
            nums.sort()
            l,r = 0 , len(nums) - 1
            
            
            while r >= l:
                mid = (l + r) // 2 

                if target > nums[mid]:
                    l = mid + 1
                    

                elif nums[mid] > target:
                    r = mid - 1


                else:
                    return mid

            return -1 



"""
nums=[-1,0,3,5,9,12]
       l     mid   r  

"""