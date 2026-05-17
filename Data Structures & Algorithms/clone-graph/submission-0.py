"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        hmap = {}

        def dfs(n):
            curr = Node(n.val)
            hmap[n.val] = curr

            for neighbor in n.neighbors:
                if neighbor.val in hmap:
                    curr.neighbors.append(hmap[neighbor.val])
                else:
                    curr.neighbors.append(dfs(neighbor))

            return curr
        
        return dfs(node)