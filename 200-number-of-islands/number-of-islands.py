class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs (row, column):
            queue = []
            queue.append((row, column))
            visited.add((row, column))

            while queue:
                row, column = queue.pop(0)

                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, column + dc

                    if(r in range(rows) and c in range(columns) and grid[r][c] == '1' and (r, c) not in visited):
                        queue.append((r, c))
                        visited.add((r, c))
        
        visited = set()
        islands = 0

        rows, columns = len(grid), len(grid[0])

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1" and (row, column) not in visited:
                    bfs(row, column)
                    islands += 1
        
        return islands
