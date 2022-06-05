# input: martix of letters
# target word
# traverse the array to see if the word is in the matrix
# GOAL: return True if in the matrix return False if not

# get the char to serach for from the target word
# search the matrix for the char
# if matrix[i][j]==char then move char being serached for to the next index
# search all adject neighbors that wasn't visited
# continue until no more word or all neighbors is not the char we're looking for
# fi no more word return True
# if traverse finishes then return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS
               or word[i] != board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1) or 
                  dfs(r - 1, c, i + 1) or
                  dfs(r, c + 1, i + 1) or
                  dfs(r, c - 1, i + 1))
            path.remove((r,c))
            
            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
                
        return False

        