"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}
        curr = head
        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        
        for i in hashmap:
            node = hashmap[i]
            
            random = hashmap[i.random] if i.random else None
            next = hashmap[i.next] if i.next else None
            
            node.random = random
            node.next = next
            
        return list(hashmap.values())[0] if len(hashmap.values()) >= 1 else None


        