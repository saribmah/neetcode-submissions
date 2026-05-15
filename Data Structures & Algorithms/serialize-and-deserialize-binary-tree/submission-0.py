# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        s = "(" + str(root.val) + ")()/"

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                s += "(" + str(node.left.val) + ")"
                queue.append(node.left)
            else:
                s += "()"
            if node.right:
                s += "(" + str(node.right.val) + ")"
                queue.append(node.right)
            else:
                s += "()"
            s += "/"
        return s[:-1]

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data: return None
        dummy = TreeNode()

        splits = data.split("/")
        child = deque([])

        for split in splits:
            nums = split.split(')(')
            num1 = nums[0][1:]
            num2 = nums[1][:-1]
            child.append(num1)
            child.append(num2)

        node_q = deque([dummy])

        while node_q:
            node = node_q.popleft()
            if not node: continue
            left = child.popleft()
            right = child.popleft()
            node.left = TreeNode(left) if left else None
            node.right = TreeNode(right) if right else None
            node_q.append(node.left)
            node_q.append(node.right)

        return dummy.left