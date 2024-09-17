class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        upperR, bottR = 0, rows - 1

        while upperR <= bottR:
            middleR = (upperR + bottR)//2

            if target > matrix[middleR][-1]:
                upperR = middleR + 1
            elif target < matrix[middleR][0]:
                bottR = middleR - 1
            else:
                break
        
        if not(upperR <= bottR):
            return False
        
        row = (upperR + bottR)//2
        left, right = 0, cols - 1

        while left <= right:
            middle = (left + right) // 2

            if matrix[row][middle] == target:
                return True
            elif target > matrix[row][middle]:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
        