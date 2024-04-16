class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        q = collections.deque()
        
        def bfs(row, col):
            nonlocal num
            print(f"processing {row}, {col}")
            num += 1
            q.append((row, col))
            visited.add((row, col))
            while(q):
                row, col = q.popleft()
                # append all the adjacents to the queue
                if((row + 1 < rows) and (grid[row+1][col] == '1') and ((row+1, col) not in visited)):
                    print(f"appending {row+1}, {col}")
                    q.append((row + 1, col))
                    visited.add((row+1, col))
                if((col + 1 < cols) and grid[row][col + 1] == '1' and ((row, col+1) not in visited)):
                    q.append((row, col + 1))
                    visited.add((row, col+1))

                if((row - 1 >= 0) and grid[row-1][col] == '1' and ((row-1, col) not in visited)):
                    q.append((row - 1, col))
                    visited.add((row-1, col))

                if((col - 1 >= 0) and grid[row][col-1] == '1' and ((row, col-1) not in visited)):
                    q.append((row, col - 1))
                    visited.add((row, col-1))

                    
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == '1' and (row, col) not in visited):
                    bfs(row, col)
        return num

#ugly solution but it works and I didn't get help
# time complexity is O(n x m)
# space complexity is O(n x m)
