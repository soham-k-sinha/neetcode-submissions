class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        _map = {}

        for n in nums:
            if n in _map:
                _map[n] += 1
                return True
            else:
                _map[n] = 1

        return False