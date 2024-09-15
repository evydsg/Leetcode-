class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            middle = (top + bot)//2

            if target > matrix[middle][-1]:
                top = middle + 1
            elif target < matrix[middle][0]:
                bot = middle - 1
            else:
                break
        
        if not(top <= bot):
            return False
        
        row = (top + bot) // 2
        left, right = 0, cols-1

        while left <= right:
            middle = (left + right) // 2

            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        
        return False
        