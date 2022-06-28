class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_dict = set()
        email_count = 0
        for email in emails:
            splitted_email = email.split("@")
            temp = ""
            for char in splitted_email[0]:
                if char == ".":
                    pass
                elif char == "+":
                    break
                else:
                    temp += char
                
            temp += "@" + splitted_email[1]
            
            if temp not in email_dict:
                email_dict.add(temp)
        
        return len(email_dict)