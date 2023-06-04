class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if (
                    board[r][c] in rows[r] 
                or board[r][c] in cols[c] 
                or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True

# Make 3 distinct sets (collections default dicts for rows, col, squares)
# Iterate and check if return false if it's inside, if not add item
# Return true end of iteration

# Time Complexity: O(n^2) time (r x c)
