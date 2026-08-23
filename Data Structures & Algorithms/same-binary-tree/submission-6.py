# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 and node2:
                if node1.val != node2.val:
                    return False
            else:
                if node1 == node2:
                    continue
                else:
                    return False

            stack1.append(node1.left)
            stack1.append(node1.right)
            stack2.append(node2.left)
            stack2.append(node2.right)
        
        return len(stack1) == len(stack2)