# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            level_length = len(q)
            for i in range(level_length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:    
                    q.append(node.right)

                if i == level_length - 1:
                    res.append(node.val)

        return res






        """
        1. basically return every right node
        2. return every left node where its right pair is null
        """