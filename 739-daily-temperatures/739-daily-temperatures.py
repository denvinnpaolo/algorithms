# temp array denotes temp at a given day
# temp has int elements
# 1 <= n <= 10^5
# Goal: return the result of how many days will it take for the the temp to get warmer from our current position



class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        s = []
        for i, t in enumerate(temps):
            while s and t > s[-1][0]:
                stackT, stackIdx = s.pop()
                
                res[stackIdx] = (i - stackIdx)
            s.append([t, i])
            
            
            
        return res