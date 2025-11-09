class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            max_row = max(range(m), key=lambda i: mat[i][mid])
            
            left_bigger = mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]
            right_bigger = mid < n - 1 and mat[max_row][mid + 1] > mat[max_row][mid]
            
            if not left_bigger and not right_bigger:
                return [max_row, mid]  # pic trouvé
            elif left_bigger:
                right = mid - 1
            else:
                left = mid + 1
        