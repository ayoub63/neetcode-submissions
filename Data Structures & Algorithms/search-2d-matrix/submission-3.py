class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        
        while bottom >= top:
            matrix_middle = (top + bottom) // 2
            if target < matrix[matrix_middle][0]:
                bottom = matrix_middle - 1
            elif target > matrix[matrix_middle][-1]:
                top = matrix_middle + 1
            else:
                break
                

        if top > bottom:
            return False
            
        found_row = (top + bottom) // 2
        l, r = 0, cols - 1
        while r >= l:
            mid = (l + r) // 2 
            if target > matrix[found_row][mid]:
                l = mid + 1 
            elif target <  matrix[found_row][mid]:
                r = mid - 1   
            else: 
                return True

        return False             
            
