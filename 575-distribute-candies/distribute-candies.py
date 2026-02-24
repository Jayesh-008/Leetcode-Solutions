class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType) // 2  
        unique_types = len(set(candyType))  
        return min(n, unique_types)




        