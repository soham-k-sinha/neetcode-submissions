"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        head = node
        seen = set()
        toSee = [node]
        nodes = defaultdict(list) # old -> [new, [old neighbours]]
        
        while toSee:
            node = toSee.pop()
            if not node:
                continue
            
            if node in seen:
                continue
            
            nodes[node].append(Node(node.val))
            if node.neighbors:
                nodes[node].append([])
                for n in node.neighbors:
                    nodes[node][1].append(n)
                    toSee.append(n)
            
            seen.add(node)
        
        for n in nodes:
            newNode = nodes[n][0]
            oldNeighbours = nodes[n][1] if len(nodes[n]) == 2 else []
            for o in oldNeighbours:
                newNode.neighbors.append(nodes[o][0])


        return nodes[head][0]

            
            
            
