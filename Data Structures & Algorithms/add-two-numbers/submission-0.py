# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # store the 2 numbers as strings (LIFO)
        # convert to integers, add and then back to string
        # add to linked list in reverse order

        n1, n2 = "", ""
        
        curr = l1
        while curr:
            n1 = str(curr.val) + n1
            curr = curr.next
        
        curr = l2
        while curr:
            n2 = str(curr.val) + n2
            curr = curr.next

        n1, n2 = int(n1), int(n2)
        res = str(n1+n2)[::-1]

        head = ListNode(res[0])
        curr = head

        for i in res[1:]:
            node = ListNode(i)
            curr.next = node
            curr = node

        return head