# Longest Valid Parenthesis

# Description:
# Given a string containing just the characters '(' and ')', find the 
# length of the longest valid (well-formed) parentheses substring.

# Constraints:
#   0 <= s.length <= 3 * 104
#   s[i] is '(', or ')'.

# Result:
# Runtime: 36 ms, faster than 97.03% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.9 MB, less than 28.61% of Python3 online submissions for Longest Valid Parentheses.


# Solution


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # check if string length is more than 1
        if len(s) == 1:
            return 0
        
        # stack
        st = [-1]
        longest = 0
        
        for idx, val in enumerate(s):
            # append the index of the open parenthesis
            if val == '(':
                st.append(idx)
            else:
                # pop stack if it's the closed parentheis ---> will either give a new starting point or
                # have a new longest
                st.pop()
                if not st:
                    # new starting point
                    st.append(idx)
                else:
                    # new longest
                    if idx - st[-1] > longest:
                        longest = idx - st[-1] 
                    
        return longest
                