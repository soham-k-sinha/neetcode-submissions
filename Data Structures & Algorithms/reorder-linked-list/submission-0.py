# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr = []
        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next
        
        s, f = 1, len(arr) - 1
        while s <= f:
            print(s, f)
            if f == s:
                head.next = arr[f]
                head = head.next
                break
            
            head.next = arr[f]
            head = head.next
            head.next = arr[s]
            head = head.next

            s += 1
            f -= 1

        head.next = None
