from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Edge case: starting point or ending point is blocked
        if grid[0][0] != 0 or grid[rows - 1][cols - 1] != 0:
            return -1

        visited = set()
        
        def bfs(row, col):
            queue = [(row, col)]
            visited.add((row, col))
            length = 1  # Start length at 1 because the first cell itself is counted
            
            while queue:
                for _ in range(len(queue)):
                    R, C = queue.pop(0)
                    
                    if R == rows - 1 and C == cols - 1:  # Check if we've reached the destination
                        return length
                    
                    # All 8 possible directions for movement in a binary matrix
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
                    for dr, dc in directions:
                        newR, newC = R + dr, C + dc
                        
                        if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == 0 and (newR, newC) not in visited:
                            queue.append((newR, newC))
                            visited.add((newR, newC))
                
                length += 1  # Increment the path length after each BFS level
            
            return -1  # Return -1 if there’s no path
        
        return bfs(0, 0)

