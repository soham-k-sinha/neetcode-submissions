# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        # returns the height of a node and also calculates the max diameter along the way
        def dfs(curr):
            if not curr:
                return 0
            
            # We make sure to bubble down to the bottom first and then come up
            left = dfs(curr.left)
            right = dfs(curr.right)

            # left + right is the diameter of the tree passing through that node
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return self.res
            