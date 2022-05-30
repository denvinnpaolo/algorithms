class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        submatrix = None
        
        for row in matrix:
            if row[0] == target or row[len(row) - 1] == target:
                return True
            if target > row[0] and target < row[len(row) - 1]:
                submatrix = row
                break
        if not submatrix:
            return False
        
        l = 0
        r = len(submatrix)
        while l <= r:
            mid = (l + r) // 2

            if submatrix[mid] == target:
                return True
            elif submatrix[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return False