class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = []

        for row in matrix:
            for value in row:
                flat_list.append(value)


        l, r = 0, len(flat_list) - 1

        while r >= l:
            m = (l + r) // 2

            if target > flat_list[m]:
                l = m + 1

            elif target < flat_list[m]:
                r = m - 1

            else: 
                return True

        return False   
