class Solution(object):
    def sumOfUnique(self, nums):
        count = 0
        for i in nums:
            if nums.count(i) == 1:
                count += i
        return count
            
        
        