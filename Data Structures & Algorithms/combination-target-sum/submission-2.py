class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(sol, i, total):
            if total > target or i >= len(nums):
                return
            
            if total == target:
                res.append(sol[:]) # or sol.copy()
                return

            # Try adding same element to list
            sol.append(nums[i])
            dfs(sol, i, total + nums[i])
            sol.pop()

            # Never add same element from now
            dfs(sol, i+1, total)
            
        

        dfs([], 0, 0)
        return res

