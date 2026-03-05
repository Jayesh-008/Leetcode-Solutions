class Solution(object):
    def findDisappearedNumbers(self, nums):
        x = set(nums)
        c = []
        for i in range(1,len(nums)+1):
            if i not in x:
                c.append(i)
        return c




        
        