class Solution(object):
    def countKeyChanges(self, s):
        count = 0
        n = len(s)
        s = s.lower()
        for i in range(0,n-1):
            if s[i] != s[i+1]:
                count += 1
        return count

        
       

        

        