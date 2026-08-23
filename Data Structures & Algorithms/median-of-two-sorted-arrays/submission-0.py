class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        total = len(nums1) + len(nums2)
        target_idx = total // 2

        all_nums = []
        while len(all_nums) < total:
            if len(nums1) != 0 and len(nums2) != 0:
                if nums1[0] < nums2[0]:
                    all_nums.append(nums1.pop(0))
                else:
                    all_nums.append(nums2.pop(0))
            elif len(nums1) == 0:
                all_nums.extend(nums2)
            else:
                all_nums.extend(nums1)
        if len(all_nums) % 2 != 0:
            return float(all_nums[target_idx])
        return (all_nums[target_idx] + all_nums[target_idx - 1]) / 2