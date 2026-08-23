# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        # Return height, but also keep track of balanced (res) along the way
        def dfs(curr):
            nonlocal res
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            height = 1 + max(left, right)
            
            if not res:
                return height
            
            res = abs(left - right) <= 1
            return height
        
        dfs(root)
        return res
            
# Can do better because, the program doesn't stop