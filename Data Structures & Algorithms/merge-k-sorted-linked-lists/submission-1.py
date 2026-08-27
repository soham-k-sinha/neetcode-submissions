# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        minHeap = []
        counter = 0

        for i in lists:
            if i:
                minHeap.append((i.val, counter, i))
                counter += 1
        heapq.heapify(minHeap)

        counter = 0
        while minHeap:
            nextMin = heapq.heappop(minHeap)[2]
            curr.next = nextMin

            if nextMin.next:
                heapq.heappush(minHeap, (nextMin.next.val, counter, nextMin.next))
            
            curr = curr.next
            counter += 1
        
        curr.next = None

        return dummy.next

