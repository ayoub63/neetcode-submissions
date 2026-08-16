# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min = float("-inf")
        max = float("inf")
        def dfs(root, min, max):
            if root is None:
                return True
            if root and (root.val >= max  or root.val <= min):
                return False
            left = dfs(root.left, min, root.val)
            right = dfs(root.right, root.val, max)
        
            return left and right

        return dfs(root, min, max)



    
        

        