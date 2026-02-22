class Solution(object):
    def isPerfectSquare(self, num):
        import math
        a = int(math.sqrt(num))
        if a*a == num:
            return True
        return False




        