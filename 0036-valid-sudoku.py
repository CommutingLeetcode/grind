class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        colSets = [set() for i in range(9)] # 9 ^ 6 total values
        rowSets = [set() for i in range(9)]
        boxSets = [set() for i in range(9)]
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                boxIndex = (row // 3) * 3 + (col //3)
                # skip if it's a '.'
                if value == ".":
                    continue
                
                # return False if found in one of 3 sets
                if value in rowSets[row] or value in colSets[col] or value in boxSets[boxIndex]:
                    print(row, col)
                    return False
                
                # not found, persist to all 3 sets
                rowSets[row].add(value)
                colSets[col].add(value)
                boxSets[boxIndex].add(value)
        
        return True
'''
easy problem
time complexity = O(9^2)
space complexity = O(9 ^ 6)
'''
