from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def bfs(root):
            
            q = deque([root])
            while q:
                if root is None:
                    return []
                
                level_length = len(q)
                level = []
                for _ in range(level_length):
                   node = q.popleft()
                   level.append(node.val) 
                   if node.left:
                      q.append(node.left)  
                   if node.right:
                      q.append(node.right) 

                levels.append(level)

            return levels

        return bfs(root)    




