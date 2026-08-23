# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s, f = head, head
        steps = 0
        while steps < n:
            f = f.next
            steps += 1
        # difference of n steps between s and f

        prev = None
        while f:
            prev = s
            s = s.next
            f = f.next
        
        if prev:
            prev.next = s.next
            return head
        return head.next
        


        