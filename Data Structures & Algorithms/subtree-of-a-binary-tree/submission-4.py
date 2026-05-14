# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False

        if not subRoot: return True

        def compareTree(t1: Optional[TreeNode], t2: Optional[TreeNode]):
            if not t1 and not t2: return True

            if not t1 or not t2: return False

            return t1.val == t2.val and compareTree(t1.left, t2.left) and compareTree(t1.right, t2.right)

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.val == subRoot.val:
                if compareTree(node, subRoot): return True

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return False

