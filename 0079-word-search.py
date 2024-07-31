class Solution:
    def __init__(self):
        self.flag = False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row, col, i, visited):
            # base case
            currString = ''.join(curr)
            if currString == word:
                self.flag = True
                return

            # do dfs on neighboring cells
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dx, dy in directions:
                newRow = row + dx
                newCol = col + dy
                if newRow >= 0 and newRow < m and newCol >= 0 and newCol < n and board[newRow][newCol] == word[i + 1] and (newRow, newCol) not in visited:
                    visited.add((newRow, newCol))
                    curr.append(board[newRow][newCol])
                    dfs(newRow, newCol, i + 1, visited)
                    visited.remove((newRow, newCol))
                    curr.pop()
        
        m = len(board)
        n = len(board[0])
        curr = []
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    curr.append(board[row][col])
                    dfs(row, col, 0, set([(row, col)]))
                    curr.pop()
                    if self.flag:
                        return True
        return False
'''
not the most efficient solution in terms of space complexity because we're using additional visited set
time complexity: there are max 4 differenct choices you can make for each cell, making it O(4^k) where k is length of word
'''
       
