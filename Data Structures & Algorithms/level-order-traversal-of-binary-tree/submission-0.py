from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:      
        levels = []
        def bfs(root):
            q = deque()
            q.append(root)
            
            while q:
                level_size = len(q)
                level = []
                for _ in range(level_size): 
                    
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                levels.append(level)
            return level
    
        levels.append(bfs(root))
        return levels




