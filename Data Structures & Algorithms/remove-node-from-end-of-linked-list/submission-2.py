# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Count length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        node_to_remove = length - n
        ind = 0
        curr = head
        prev = None
        while curr:
            if ind == node_to_remove:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            prev = curr
            curr = curr.next
            ind += 1
        
        return head