class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        min_ind = 0
        while l <= r:
            if nums[l] < nums[r]:
                if nums[l] < nums[min_ind]:
                    min_ind = l
                break
            m = (l + r) // 2
            if nums[m] < nums[min_ind]:
                min_ind = m
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        l1, r1, l2, r2 = 0, min_ind - 1, min_ind, len(nums) - 1
        
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if target > nums[m1]:
                l1 = m1 + 1
            elif target < nums[m1]:
                r1 = m1 - 1
            else:
                return m1

        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if target > nums[m2]:
                l2 = m2 + 1
            elif target < nums[m2]:
                r2 = m2 - 1
            else:
                return m2

        return -1