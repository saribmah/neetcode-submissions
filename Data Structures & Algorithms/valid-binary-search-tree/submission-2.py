# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        queue = deque([(float('-inf'), float('inf'), root)])

        while queue:
            left, right, node = queue.popleft()

            if not (left < node.val < right):
                return False

            if node.left:
                queue.append((left, node.val, node.left))
            if node.right:
                queue.append((node.val, right, node.right))
            
        return True
