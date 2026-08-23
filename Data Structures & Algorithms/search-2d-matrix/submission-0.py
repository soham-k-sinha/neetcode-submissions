class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        extended = []
        for r in matrix:
            extended.extend(r)
        
        l, r = 0, len(extended) - 1
        while l <= r:
            m = (l + r)//2
            if target > extended[m]:
                l = m + 1
            elif target < extended[m]:
                r = m - 1
            else:
                return True
        return False
        