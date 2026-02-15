class Solution(object):
    def countDigits(self, num):
        count = 0
        b = num
        while(num > 0):
            a = num % 10
            if b % a == 0:
                count += 1
            num //= 10
        return count
      
    
       
        