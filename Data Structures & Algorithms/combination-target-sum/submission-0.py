class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(sol, i):
            if sum(sol) > target or i >= len(nums):
                return
            
            if sum(sol) == target:
                res.append(sol[:]) # or sol.copy()
                return

            sol.append(nums[i])
            dfs(sol, i)
            sol.pop()

            dfs(sol, i+1)
            
        

        dfs([], 0)
        return res

