# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q: return None
        queue = deque([root])

        while queue:
            node = queue.popleft()

            lower = min(p.val, q.val)
            higher = max(p.val, q.val)

            if lower <= node.val and higher >= node.val:
                return node
            elif p.val > node.val:
                queue.append(node.right)
            elif q.val < node.val:
                queue.append(node.left)
        return []