class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = self.findColumn(matrix, target)
        if col == -1:
            return False
        l = 0
        r = len(matrix[col]) - 1
        
        while(l <= r):
            mid = (l + r) // 2
            if matrix[col][mid] == target:
                return True
            elif matrix[col][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False




    def findColumn(self, matrix: List[List[int]], target: int) -> int:
            top = 0
            bottom = len(matrix) - 1

            while(top <= bottom):
                mid = (bottom + top) // 2
                curr_row_max = max(matrix[mid])
                if matrix[mid][0] == target or curr_row_max == target:
                    return mid
                elif target > matrix[mid][0] and target < curr_row_max:
                    return mid
                elif target >  curr_row_max:
                    top = mid + 1
                else: 
                    bottom = mid - 1
            return -1



                    