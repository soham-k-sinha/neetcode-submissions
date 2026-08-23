class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l, r = 0, (m * n) - 1
        while l <= r:
            mid = (l + r)//2
            mid_row = mid // n
            mid_col = mid % n
            if target > matrix[mid_row][mid_col]:
                l = mid + 1
            elif target < matrix[mid_row][mid_col]:
                r = mid - 1
            else:
                return True
        return False

        # there are m * n elements so binary search takes O(log(m*n)) time
        