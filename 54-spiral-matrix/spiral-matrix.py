class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]), 0, len(matrix)
        result = []

        while left < right and top < bottom:
            for index in range(left, right):
                result.append(matrix[top][index])
            top += 1

            for index in range(top, bottom):
                result.append(matrix[index][right-1])
            right -= 1

            if not(left < right and top < bottom):
                break
            
            for index in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][index])
            bottom -= 1

            for index in range(bottom-1, top-1, -1):
                result.append(matrix[index][left])
            left += 1
        
        return result

        