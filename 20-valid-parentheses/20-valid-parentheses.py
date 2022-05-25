class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        
        openBrackets = []
        
        for bracket in s:
            if bracket == "[" or bracket == "{" or bracket == "(":
                openBrackets.append(bracket)
            else:
                if len(openBrackets) > 0:
                    if bracket == ")" and openBrackets[-1] =="(":
                        openBrackets.pop()
                    elif bracket == "}" and openBrackets[-1] == "{":
                        openBrackets.pop()
                    elif bracket == "]" and openBrackets[-1] == "[":
                        openBrackets.pop()
                    else:
                        break
                else: return False
                    
        if len(openBrackets) > 0:
            return False
        return True