class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        seen = set()

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        print(adj)

        def dfs(node, parent):
            if node in seen:
                return

            seen.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        total = 0
        for i in range(n):
            if i in seen:
                continue
            print("new loop")
            total += 1
            dfs(i, -1)

        return total