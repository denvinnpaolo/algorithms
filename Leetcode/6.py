# Zigzag Conversion

# desc: The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # check if row is one because if it's not then no need to do zigzag pattern
        if numRows == 1:
            return s
        
        # hashmap using row number as key and its value as the chars combined
        d = dict(zip([x + 1 for x in range(numRows)], ['' for x in range(numRows)]))
       
        counter = 1
        reverse = False
        
        for c in s:
            # check if it's on top
            if counter == 1:
                d[counter] += c
                counter += 1
                if reverse:
                    reverse = False
            # check if it's at the bottom
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



# result:
# Runtime: 52 ms, faster than 92.27% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14.7 MB, less than 13.71% of Python3 online submissions for Zigzag Conversion.
