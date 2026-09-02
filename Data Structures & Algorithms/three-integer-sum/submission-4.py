class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        for i1 in range(len(nums)-2):
            hashmap = {}
            num1 = nums[i1]

            for i2 in range(i1+1, len(nums)):
                num2 = nums[i2]
                if num2 in hashmap:
                    toAdd = sorted([num1, num2, hashmap[num2]])
                    if tuple(toAdd) in seen:
                        continue
                    res.append(toAdd)
                    seen.add(tuple(toAdd))
                    continue
                else:
                    lookingFor = -(num2 + num1)
                    hashmap[lookingFor] = num2
        
        return res