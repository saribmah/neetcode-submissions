# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lot = []

        def dfs(root: Optional[TreeNode], level: int):
            if not root: return None

            if len(lot) < level: lot.append([])

            lot[level-1].append(root.val)

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root, 1)
        return lot