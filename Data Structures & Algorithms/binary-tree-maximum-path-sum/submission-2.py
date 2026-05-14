# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float('-inf')

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_sum
            if not node: return 0

            nv = node.val
            lnv = max(dfs(node.left), 0)
            rnv = max(dfs(node.right), 0)

            max_sum = max(node.val + lnv + rnv, max_sum) 

            return node.val + max(lnv, rnv)

        dfs(root)

        if max_sum == float('-inf'): return 0

        return max_sum