class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        def union(a, b):
            aRep = find(a)
            bRep = find(b)

            if rank[aRep] > rank[bRep]:
                parent[bRep] = aRep
                rank[aRep] += 1
            else:
                parent[aRep] = bRep
                rank[bRep] += 1

        def find(a):
            while a != parent[a]:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        for (a, b) in edges:
            union(a, b)
        
        return len(set(find(x) for x in range(n)))
