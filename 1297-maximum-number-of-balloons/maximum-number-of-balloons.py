class Solution(object):
    def maxNumberOfBalloons(self, text):
        b = text.count('b')
        a = text.count('a')
        l = text.count('l')//2
        o = text.count('o')//2
        n = text.count('n')
        
        return min(a,b,o,l,n)

       
        
        