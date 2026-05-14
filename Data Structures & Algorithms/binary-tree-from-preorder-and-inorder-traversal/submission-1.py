# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder: return None

        node = TreeNode(preorder[0])

        target = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:target+1], inorder[:target])
        node.right = self.buildTree(preorder[target+1:], inorder[target+1:])

        return node
        