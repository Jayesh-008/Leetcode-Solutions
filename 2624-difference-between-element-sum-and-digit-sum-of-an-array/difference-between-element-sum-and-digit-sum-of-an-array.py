class Solution(object):
    def differenceOfSum(self, nums):
        count1 = 0
        count2 = 0
        for i in nums:
            count1 += i
            while i > 0:
                count2 += i % 10
                i = i // 10
          
        return count1 - count2

       
        