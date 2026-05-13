# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None: return head
        prev = None
        while head:
            curr = head.next
            head.next = prev
            prev = head
            if curr is not None:
                head = curr
            else:
                break
        return head
