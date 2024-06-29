class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v].append(u)

        def dfs(node: int, visited: Set[int], ancestors: Set[int]):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    ancestors.add(neighbor)
                    dfs(neighbor, visited, ancestors)
        
        res = []
        for i in range(n):
            ancestors = set()
            dfs(i, set(), ancestors)
            res.append(sorted(ancestors))
        
        return res
