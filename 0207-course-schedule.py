class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make an inDegree array
        inDegree = [0 for _ in range(numCourses)]
        # make an adjacency list
        adjacency = [[] for _ in range(numCourses)]
        
        for incoming, out in prerequisites:
            adjacency[out].append(incoming)
            inDegree[incoming] += 1
        
        queue = []
        # add all nodes that have 0 inDegrees
        for index, degree in enumerate(inDegree):
            if degree == 0:
                queue.append(index)
        
        counter = 0
        while(queue):
            popped = queue.pop(0)
            counter += 1
            for neighbour in adjacency[popped]:
                inDegree[neighbour] -= 1
                if inDegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return counter == numCourses
        
'''
we're using a topological sort approach. Basically saying if the topological sorted array doesn't exist, means that we have a cycle in our graph. This is cleverly done by appending all the nodes with 0 inDegrees and appending it to our queue
the time complexity for this approach is O(V + E) done for creating the adjacency list and proccesing our queue. Basically we're dequeing each node only once, and we're processing all its neighbours consequently only once. 
'''
