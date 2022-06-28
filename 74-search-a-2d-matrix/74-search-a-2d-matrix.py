class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            sub_matrix = None
            for row in matrix:
                if row[-1] >= target:
                    sub_matrix = row
                    break
            
            print(sub_matrix)
            if not sub_matrix: return False
            
            l = 0
            r = len(sub_matrix) - 1
            
            print(sub_matrix)
            while l <= r:
                mid = (l + r) // 2
                
                num = sub_matrix[mid]
                print(num, target)
                if num  == target:
                    return True
                elif num < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False