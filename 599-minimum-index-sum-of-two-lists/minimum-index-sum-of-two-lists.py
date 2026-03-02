class Solution(object):
    def findRestaurant(self, list1, list2):
        min_sum = float('inf')
        result = []
        
        for i in list1:
            if i in list2:
                total = list1.index(i) + list2.index(i)
                
                if total < min_sum:
                    min_sum = total
                    result = [i]
                elif total == min_sum:
                    result.append(i)
        
        return result
        
        