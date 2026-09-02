class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]

        i1 = 0
        while i1 < len(nums) - 1:
            l, r = i1+1, len(nums) - 1

            if i1 > 0 and nums[i1] == nums[i1-1]:
                i1 += 1
                continue
            
            while l < r:
                target = -nums[i1]
                if nums[l] + nums[r] == target:
                    res.append([nums[i1], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            
            i1 += 1
            
        return res