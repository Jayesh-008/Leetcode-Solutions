class Solution(object):
    def findNumbers(self, nums):
        
        count2 = 0
        for i in nums:
            count1 = 0
            while i>0:
                count1 += 1
                i = i // 10
            if count1 % 2 == 0:
                count2 += 1
        return count2
                

        
        