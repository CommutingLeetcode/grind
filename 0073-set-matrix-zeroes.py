class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        # all rows that need to have all its cells changed to 0
        rowChange = set()
        # all columns that have to be changed to 0
        colChange = set()
        # first pass: figure out where the 0s are
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    rowChange.add(row)
                    colChange.add(col)

        # second pass: modify the matrix
        for row in range(m):
            for col in range(n):
                if row in rowChange or col in colChange:
                    matrix[row][col] = 0

        
        
'''
time = O(m * n) where m is rows and n is cols

'''
