# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_nums = []

        def dfs(root: Optional[TreeNode]):
            if not root: return None

            dfs(root.left)
            sorted_nums.append(root.val)
            dfs(root.right)

        dfs(root)

        return sorted_nums[k-1]