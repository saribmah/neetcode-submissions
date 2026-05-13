# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None: return head
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        head = stack.pop()
        curr = head
        while len(stack):
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        return head