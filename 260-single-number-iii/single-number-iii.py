class Solution(object):
    def singleNumber(self, nums):
        a = []
        for num in nums:
            if nums.count(num) == 1:
                a.append(num)
        return a

    
        
        