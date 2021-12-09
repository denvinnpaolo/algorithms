# Multiply Strings



# Description
# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the 
# inputs to integer directly.



# Constraints
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# Results
# Runtime: 44 ms, faster than 61.81% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.2 MB, less than 83.49% of Python3 online submissions for Multiply Strings.


# Solution
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        prod = str(self.getStrToInt(num1) * self.getStrToInt(num2))
        
        return prod
        
            
    def getStrToInt(self, num):
        s = 0
        for i, val in enumerate(reversed(num)):
            if i == 0:
                s +=self.stringVal(ord(val))
                
            else:
                digitPlace = pow(10, i)
                
                s+= (digitPlace * self.stringVal(ord(val)))
            
        return s
    
    def stringVal(self, num):
        d ={
            48: 0,
            49: 1,
            50: 2,
            51: 3,
            52: 4,
            53: 5,
            54: 6,
            55: 7,
            56: 8,
            57: 9
        }
        
        return d[num]
        
        