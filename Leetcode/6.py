# Zigzag Conversion

# desc: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        d = dict(zip([x + 1 for x in range(numRows)], ['' for x in range(numRows)]))
       
        counter = 1
        reverse = False
        
        for c in s:
            if counter == 1:
                d[counter] += c
                counter += 1
                if reverse:
                    reverse = False
            elif counter == numRows:
                d[counter] += c
                counter -= 1
                if not reverse: 
                    reverse = True

            else: 
                d[counter] += c
                
                if not reverse:
                    counter += 1
                if reverse:
                    counter -= 1
        
        res = ''
        for n in range(numRows):
            res += d[n + 1]
            
        return res


