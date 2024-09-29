class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            queue = [(row, col)]
            visited.add((row, col))

            while queue:
                r, c = queue.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    newR, newC = r + dr, c + dc

                    if newR in range(rows) and newC in range(cols) and grid[newR][newC] == '1' and (newR, newC) not in visited:
                        queue.append((newR, newC))
                        visited.add((newR, newC))
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and ((r, c)) not in visited:
                    bfs(r, c)
                    islands += 1
        
        return islands