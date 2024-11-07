"""
    Understand: the idea is to count how many islands we can find in the grid

    - Can we have a grid with only 1's? 
    - Can we have a grid with only 0's?
    - Can we have an empty grid?

    Match: BFS

    Plan
        - Check if the grid is empty
        - Initialize the variable to count how many islands are in the grid
        - Get the count of how many rows and cols we find the grid
        - Initialize a set to keep track of visited nodes
        - Helper function to do a bfs in the grid
        - Iterate through the rows and cols
            - Check if we have found an island and if it has not been visited yet
            - Call the helper function
            - Increment the count
    
    Evaluate
        - Time Complexity: O(m * n)
        - Space Complexity: O(m * n)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        islands, visited = 0, set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = [(row, col)]
            visited.add((row, col))

            while queue:
                r, c = queue.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    R, C = r + dr, c + dc

                    if R in range(rows) and C in range(cols) and grid[R][C] == '1' and (R, C) not in visited:
                        queue.append((R, C))
                        visited.add((R, C))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
        