# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Slow and fast pointer approach
        # Move f n steps
        # then move f and s one step at a time until f reaches one node before end (last node)
        # s now represents the node before the node we want to remove
        s, f = head, head
        steps = 0
        while steps < n:
            f = f.next
            steps += 1

        if not f:
            return head.next
        
        while f.next:
            f = f.next
            s = s.next

        s.next = s.next.next
        return head
        
        

        

        