class Solution(object):
    def subtractProductAndSum(self, n):
        count1 = 0
        count2 = 1
        while(n != 0):
            count1 += n%10
            count2 *= n%10
            n = n//10
        return count2 - count1
        
   
        