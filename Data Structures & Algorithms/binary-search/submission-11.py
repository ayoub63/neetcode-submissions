class Solution:
    def search(self, nums: List[int], target: int) -> int:
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


# initialize two pointers
# compute middle index 
# if bigger than middle cut search space in half from left, if smaller from right
# compute middle again this time its middle of the new search space