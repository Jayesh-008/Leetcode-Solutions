class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip() # 1. Remove leading whitespace
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # 2. Handle sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        res = 0
        # 3. Convert digits
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        res *= sign
        
        # 4. Clamping to 32-bit signed integer range
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        if res < MIN_INT:
            return MIN_INT
        if res > MAX_INT:
            return MAX_INT
            
        return res
        