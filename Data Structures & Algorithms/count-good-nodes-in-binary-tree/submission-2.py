# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, highest):
            if not node:
                return 0
            is_good = 1 if node.val >= highest else 0
            highest = max(highest, node.val)
            return is_good + dfs(node.left, highest) + dfs(node.right, highest)

        return dfs(root, float("-inf"))