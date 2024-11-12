class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid[0])-1] != 0:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            length = 1
            queue = [(row, col)]
            visited.add((row, col))

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.pop(0)

                    if r == rows - 1 and c == cols - 1:
                        return length
                    
                    directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

                    for dr, dc in directions:
                        R, C = r + dr, c + dc

                        if 0 <= R < rows and 0 <= C < cols and grid[R][C] == 0 and ((R, C)) not in visited:
                            queue.append((R, C))
                            visited.add((R, C))

                length += 1

            return -1
        
        return bfs(0, 0)