class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        d = {"row":{}, "col":{}, 
             "box":{
                0: set(),
                1: set(),
                2: set(),
                3: set(),
                4: set(),
                5: set(),
                6: set(),
                7: set(),
                8: set(),
                }
        }
        
        def check_box(row, col):
            if row < 3 and col < 3:
                return d['box'][0]
            elif row < 3 and (col >2 and col < 6):
                return d['box'][1]
            elif row < 3 and col > 5:
                return d['box'][2]
            elif row > 2 and row < 6 and col < 3:
                return d['box'][3]
            elif row > 2 and row < 6 and col > 2 and col < 6:
                return d['box'][4]
            elif row > 2 and row < 6 and col > 5:
                return d['box'][5]
            elif row > 5 and col < 3:
                return d['box'][6]
            elif row > 5 and col > 2 and col < 6:
                return d['box'][7]
            elif row > 5 and col > 5:
                return d['box'][8]
                
        
        for row in range(len(board)):
            d["row"][row] = set()
            for col in range(len(board[row])):
                num = board[row][col]
                
                if col not in d["col"]:
                    d["col"][col] = set()
                    
                if board[row][col] == ".":
                    continue
                elif num in d["row"][row] or num in d["col"][col] or num in check_box(row, col):
                    return False
                else:
                    d["row"][row].add(num)
                    d['col'][col].add(num)
                    check_box(row, col).add(num)
        print(d)
        
        return True