# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = node = ListNode()
        node.next = head

        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        node_to_remove = None
        for i in range(n):
            node_to_remove = stack.pop()
        print(node_to_remove.val)
        curr = node
        while curr:
            if curr.next == node_to_remove:
                curr.next = node_to_remove.next
                break
            else:
                curr = curr.next
        if node.next:
            return node.next
        return None