class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        visited = set()
        def dfs(row, col):
            visited.add((row, col))
            # Flip O to T
            board[row][col] = "T"
            
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            for (dx, dy) in directions:
                newRow, newCol = row + dx, col + dy
                if newRow not in range(rows) or newCol not in range(cols) or (newRow, newCol) in visited or board[newRow][newCol] != "O":
                    continue
                dfs(newRow, newCol)
                

        # top and bottom row
        for col in range(cols):
            if (0, col) not in visited and board[0][col] == "O":
                dfs(0, col)
            if (rows - 1, col) not in visited and board[rows - 1][col] == "O":
                dfs(rows - 1, col)
                
        # left and right col
        for row in range(rows):
            if (row, 0) not in visited and board[row][0] == "O":
                dfs(row, 0)
            if (row, cols - 1) not in visited and board[row][cols - 1] == "O":
                dfs(row, cols - 1) 
                
        # final 2d traversal
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"

"""
Solution from neetcode, time and space complexity goes to O(m * n)
traversing the border could be easier when done like
for row in range(rows):
  for col in range(cols):
    if (row in [0, rows - 1] or col in [0, cols - 1]) and (row, colO not in visited and board[row][col] == "O":
      dfs
"""
