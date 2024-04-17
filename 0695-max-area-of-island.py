class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        q = collections.deque()
        # get number of rows and cols
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        
        def bfs(row, col):
            area = 0
            q.append((row, col))
            visited.add((row, col))
            while(q):
                row, col = q.popleft()                
                # increment area as this cell is a valid cell, not visited yet, and is a 1
                area += 1
                    
                # append all neighbours to queue
                directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in directions:
                    newRow, newCol = row+dx, col+dy
                    if((newRow, newCol) in visited or newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols or grid[newRow][newCol] == 0):
                        continue
                    q.append((newRow, newCol))
                    visited.add((newRow, newCol))
            return area;
        
        # iterate through the 2d matrix
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(bfs(row, col), maxArea)
        
        
        
        return maxArea

# This took way longer than I thought because of confusion in when to append a new node to the visited set. The answer to that is right after you append to the queue.
# Another thing is about if I should check validity before appending, or after. The answer is probably before appending so that we don't have to worry about appending nodes that are not valid
# The time complexity and same complexity is same as number-of-islands problem, O(m x n)
