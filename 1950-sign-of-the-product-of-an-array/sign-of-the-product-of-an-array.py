class Solution(object):
    def arraySign(self, nums):
        count = 1
        for i in nums:
            if i < 0:
                count *= -1
            elif i > 0:
                count *= 1
            elif  i == 0:
                count *= 0
        return count
        
        