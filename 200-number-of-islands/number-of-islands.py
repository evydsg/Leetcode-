class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            queue = [(row, col)]
            visited.add((row, col))
            
            while queue:
                ROW, COL = queue.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    R, C = ROW + dr, COL + dc

                    if R in range(rows) and C in range(cols) and grid[R][C] == '1' and (R, C) not in visited:
                        queue.append((R, C))
                        visited.add((R, C))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands
        