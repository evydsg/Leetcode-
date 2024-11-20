class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])

        def dfs(row, col):
            if row not in range(rows) or col not in range(cols) or board[row][col] != "O":
                return 
            
            board[row][col] = "N"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and row in [0, rows-1] or col in [0, cols-1]:
                    dfs(row, col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = 'X'
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'N':
                    board[row][col] = 'O'