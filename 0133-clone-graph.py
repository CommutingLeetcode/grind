"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # traverse the starting node using BFS
        oldNew = {}
        visited = set()
        q = collections.deque()
        q.append(node)
        visited.add(node)
        oldNew[node] = Node(node.val)
        while q:
            curr = q.popleft()
            currCopy = oldNew[curr]

            # append all of current node's neighbours
            for neighbor in curr.neighbors:
                if neighbor in oldNew:
                    currCopy.neighbors.append(oldNew[neighbor])
                else:
                    neighborCopy = Node(neighbor.val)
                    oldNew[neighbor] = neighborCopy
                    currCopy.neighbors.append(neighborCopy)
                    
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
        return oldNew[node]
                
"""
This is the iterative BFS solution (to change to iterative DFS, just change the queue to a stack)
Time complexity: O(n) where n is the number of nodes + number of edges
Space complexity: O(n * n-1) because each node can have at most n-1 neighbours
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldNew = {}
        def dfs(node):
            if node in oldNew:
                return oldNew[node]
            
            nodeCopy = Node(node.val)
            oldNew[node] = nodeCopy
 
            for neighbor in node.neighbors:
                nodeCopy.neighbors.append(dfs(neighbor))
            return nodeCopy
        if not node:
            return None
        return dfs(node)

"""
recursive dfs solution
"""
