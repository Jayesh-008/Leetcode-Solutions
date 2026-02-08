class Solution(object):
    def xorOperation(self, n, start):
        count = 0
        for i in range(0,n):
            count ^= start+2*i
        return count
        
            

        
        