# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next # beginning node of the second half
        s.next = None # This is going to be the last node - last node of first half

        # Reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Merge both lists

        while prev: # prev is the last node of the second list (now is the first due to reverse)
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2