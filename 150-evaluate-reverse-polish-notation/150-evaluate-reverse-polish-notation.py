class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for el in tokens:

            if el == "+":
                n1 = s.pop()
                n2 = s.pop()
                n3 = n1 + n2
                s.append(n3)
            elif el =="-":
                n1 = s.pop()
                n2 = s.pop()
                n3 = n2 - n1
                s.append(n3)
            elif el =="*":
                n1 = s.pop()
                n2 = s.pop()
                n3 = n1 * n2
                s.append(n3)
            elif el =="/":
                n1 = s.pop()
                n2 = s.pop()
                n3 = int(n2 / n1)
                s.append(n3)
            else:
                s.append(int(el))
        return s[0]