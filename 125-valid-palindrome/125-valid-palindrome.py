# inputs
# - string
#   
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        extracted_string = ""
        
        for char in lowered:
            if char.isalnum():
                extracted_string += char
        
        i = 0
        j = len(extracted_string) - 1
        
        while i <= j:
            if extracted_string[i] == extracted_string[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True