class Solution(object):
    def maximumWealth(self, accounts):
        count1 = 0
        for i in accounts:
            count2 = 0
            for j in i:
                count2 += j
            if count2 > count1:
                count1 = count2
        return count1
        
        
                   
        
        