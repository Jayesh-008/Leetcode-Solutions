class Solution(object):
    def canAliceWin(self, nums):
        count1 = 0
        count2 = 0
        for i in nums:
            if i < 10:
                count1 += i
            else:
                count2 += i  
        
        return(count1 != count2)  
      
             



        
        