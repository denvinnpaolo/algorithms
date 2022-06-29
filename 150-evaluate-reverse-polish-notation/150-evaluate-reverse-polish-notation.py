class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for el in tokens:
            if el == "+":
                s.append(s.pop() + s.pop())
            elif el =="-":
                a,b = s.pop(), s.pop()
                s.append(b-a)
            elif el =="*":
                s.append(s.pop() * s.pop())
            elif el =="/":
                a, b = s.pop(), s.pop()
                n3 = int(b / a)
                s.append(n3)
            else:
                s.append(int(el))
        return s[0]